from django.core.management.base import BaseCommand
from django.db import transaction, close_old_connections

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from datetime import datetime
import time
import concurrent.futures

from quotes_scraper.models import Author, Tag, Quote

LOGIN_URL = "https://quotes.toscrape.com/login"
BASE_URL = "https://quotes.toscrape.com/"

def parse_birth_date(text):
    if not text:
        return None
    try:
        return datetime.strptime(text.strip(), "%B %d, %Y").date()
    except Exception:
        return None

def fetch_author_details(session, author_url):
    full = author_url if author_url.startswith("http") else urljoin(BASE_URL, author_url)
    resp = session.get(full, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    name_el = soup.find("h3", class_="author-title")
    born_date_el = soup.find("span", class_="author-born-date")
    born_loc_el = soup.find("span", class_="author-born-location")

    name = name_el.get_text(strip=True) if name_el else None
    born_date = parse_birth_date(born_date_el.get_text(strip=True)) if born_date_el else None
    born_location = born_loc_el.get_text(strip=True) if born_loc_el else None

    return {
        "name": name,
        "birth_date": born_date,
        "birth_location": born_location,
        "about_url": full,
    }

class Command(BaseCommand):
    help = "Scrape https://quotes.toscrape.com (login required section) and save quotes/authors/tags to DB."

    def add_arguments(self, parser):
        parser.add_argument("--username", "-u", default="admin")
        parser.add_argument("--password", "-p", default="admin")
        parser.add_argument("--concurrency", "-c", type=int, default=1,
                            help="Number of threads to use for fetching author pages (1 = sequential).")

    def handle(self, *args, **options):
        username = options["username"]
        password = options["password"]
        concurrency = max(1, options["concurrency"])

        session = requests.Session()

        # 1) Fetch login page to obtain CSRF token
        self.stdout.write("Fetching login page to obtain CSRF token...")
        r = session.get(LOGIN_URL, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")
        token_input = soup.find("input", {"name": "csrf_token"})
        csrf_token = token_input["value"] if token_input else ""
        if not csrf_token:
            self.stdout.write(self.style.WARNING("CSRF token not found; proceeding without it."))

        # 2) Log in
        self.stdout.write(f"Logging in as {username} ...")
        login_data = {"csrf_token": csrf_token, "username": username, "password": password}
        login_resp = session.post(LOGIN_URL, data=login_data, timeout=10)
        login_resp.raise_for_status()
        self.stdout.write(self.style.SUCCESS("Login done."))

        # 3) Crawl pages and collect quotes + author links
        next_url = BASE_URL
        quotes_buffer = []
        authors_to_fetch = {}  # about_url -> name_from_list

        self.stdout.write("Crawling quote list pages...")
        page_count = 0
        while next_url:
            page_count += 1
            self.stdout.write(f"Fetching page: {next_url}")
            resp = session.get(next_url, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "lxml")

            quote_divs = soup.find_all("div", class_="quote")
            for qdiv in quote_divs:
                text_el = qdiv.find("span", class_="text")
                author_el = qdiv.find("small", class_="author")
                about_a = qdiv.find("a", href=True, text="(about)")
                tag_els = qdiv.find_all("a", class_="tag")

                quote_text = text_el.get_text(strip=True) if text_el else ""
                author_name = author_el.get_text(strip=True) if author_el else None
                author_about_href = urljoin(BASE_URL, about_a["href"]) if about_a else None
                tags = [t.get_text(strip=True) for t in tag_els] if tag_els else []

                quotes_buffer.append({
                    "text": quote_text,
                    "author_name": author_name,
                    "author_about_url": author_about_href,
                    "tags": tags,
                })

                if author_about_href and author_about_href not in authors_to_fetch:
                    authors_to_fetch[author_about_href] = author_name

            next_li = soup.find("li", class_="next")
            if next_li and next_li.a and next_li.a["href"]:
                next_url = urljoin(BASE_URL, next_li.a["href"])
            else:
                next_url = None

            time.sleep(0.1)

        self.stdout.write(self.style.SUCCESS(f"Collected {len(quotes_buffer)} quotes and {len(authors_to_fetch)} author links from {page_count} pages."))

        # 4) Fetch author pages (concurrent if requested)
        self.stdout.write("Fetching author detail pages...")
        author_details = {}

        def worker_fetch(url):
            close_old_connections()
            try:
                details = fetch_author_details(session, url)
            except Exception as e:
                self.stderr.write(f"Failed to fetch author page {url}: {e}")
                details = {"name": authors_to_fetch.get(url), "birth_date": None, "birth_location": None, "about_url": url}
            return url, details

        if concurrency == 1:
            for url in authors_to_fetch.keys():
                _, details = worker_fetch(url)
                author_details[url] = details
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as exe:
                futures = {exe.submit(worker_fetch, url): url for url in authors_to_fetch.keys()}
                for fut in concurrent.futures.as_completed(futures):
                    url, details = fut.result()
                    author_details[url] = details

        # 5) Persist to DB (idempotent)
        self.stdout.write("Saving to database (idempotently)...")
        saved_authors = saved_tags = saved_quotes = 0

        for entry in quotes_buffer:
            text = entry["text"]
            author_about_url = entry["author_about_url"]
            author_name_from_list = entry["author_name"]
            tags_list = entry["tags"]

            details = author_details.get(author_about_url, {
                "about_url": author_about_url,
                "name": author_name_from_list,
                "birth_date": None,
                "birth_location": None
            })

            with transaction.atomic():
                author_obj, created = Author.objects.update_or_create(
                    about_url=details["about_url"],
                    defaults={
                        "name": details.get("name") or author_name_from_list or "Unknown",
                        "birth_date": details.get("birth_date"),
                        "birth_location": details.get("birth_location"),
                    }
                )
                if created:
                    saved_authors += 1

                tag_objs = []
                for tname in tags_list:
                    tname_strip = tname.strip()
                    if not tname_strip:
                        continue
                    tag_obj, tag_created = Tag.objects.get_or_create(name=tname_strip)
                    tag_objs.append(tag_obj)
                    if tag_created:
                        saved_tags += 1

                quote_obj, q_created = Quote.objects.get_or_create(text=text, author=author_obj)
                if tag_objs:
                    quote_obj.tags.set(tag_objs)
                saved_quotes += 1

        self.stdout.write(self.style.SUCCESS(f"Saved: authors≈{saved_authors}, tags≈{saved_tags}, quotes≈{saved_quotes}"))
        self.stdout.write(self.style.SUCCESS("Scraping finished."))
