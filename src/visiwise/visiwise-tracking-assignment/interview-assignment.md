# On-Site Task: Django Scraper for Quotes

## 🎯 Objective

This task is designed to evaluate your ability to work within a Django project to:
- Build a web scraper that handles a multi-step process (authentication, pagination).
- Scrape and parse data from multiple page types.
- Design normalized database models using the Django ORM.
- Persist data efficiently, safely, and *idempotently*.
- Handle real-world scraping errors gracefully.
- Identify performance bottlenecks and propose solutions.

## 📦 Setup

You will be provided with a minimal Django 4.x project skeleton.

Your work should be done entirely *within* this provided project structure.

## 🔧 The Task

Your goal is to write a Django code that scrapes *all* quotes and author details from the authenticated section of the "Quotes to Scrape" site.

The target is: `https://quotes.toscrape.com/login`

### 1. Define Your Models

In `scraper/models.py`, define the Django models to store the data you will scrape.

### 2. Handle Login

The site requires a login. You must first programmatically log into the site.
- The login form is a mock form; you can use *any username and password* (e.g., `user: 'admin'`, `pass: 'admin'`).
- *Note:* The login form is protected by a *CSRF token*. You will need to correctly fetch this token and include it in your login request.

### 3. Scrape Quote & Author Data

Once logged in, you will be on the first page of quotes.

For each quote on the page, you must scrape:
- The quote text.
- The author's name.
- A list of the tags associated with the quote.

*Additionally*, there is a link after author's name (about) which is a link to the author's detail page. You must:
- Follow this link to the author's individual page.
- Scrape the author's *birthdate* and *birth location*.
- Add this data to your Author objects in the database.

---

## ⭐ Requirements

1. *Language & Framework:* All code must be written in *Python* and operate within the provided *Django project*.
2. *Data Storage:* You *must* use the Django ORM to save data.
3. *Idempotency:* The scrape code must be *idempotent*. If the code is run a second time, it must *not* create duplicate entries for quotes, authors, or tags.
4. *Error Handling:* Author detail pages may occasionally be missing data (e.g., no birth location). Your script must handle these cases *gracefully* (e.g., saving `None`/`NULL`) and continue scraping without crashing.
5. *Libraries:* You are free to use libraries like `requests` and `BeautifulSoup4`. You *must* list any external libraries you use in a `requirements.txt` file.
6. *Documentation:* You must provide a brief explanation (either as comments in your script or as a separate `README.md` file or at least prepare for a verbal description) documenting:
   - Your model design choices.
   - How you handled session management and the CSRF token.
   - *Performance Trade-off:* A simple scraper will be slow because it fetches author pages sequentially. Briefly explain the design of how you would refactor this scraper for high performance.
   - *Probing Question:* Imagine the author's name and details link on the quote list were *not* in the initial HTML, but loaded 1 second later via JavaScript. Briefly explain how you would gather this part of data and *why*.

---

## 🏆 Bonus Tasks (If you finish early)

1. *Concurrency:* Modify your management code to fetch the *parts of the data* concurrently to improve speed.
2. *Browser Automation:* Create a *separate* script (e.g., `scrape_js.py`) that uses *Selenium* or *Playwright* to scrape the quotes from `https://quotes.toscrape.com/js-delayed/`. Print the first quote's text and author to the console.

---

## 📊 Evaluation Metrics

We will be evaluating your submission based on the following criteria:

- *Correctness:* Does the code run without errors? Does the `db.sqlite3` file contain complete and accurate data from *all* pages and *all* author detail pages?
- *Database Design:* Are your Django models in `models.py` normalized, efficient, and do they correctly represent the relationships?
- *Idempotency & Efficiency:* Does the code handle being run multiple times without creating duplicates? Does the candidate demonstrate an understanding of performance bottlenecks?
- *Resilience & Fault Tolerance:* Does the code handle potential errors gracefully (e.g., missing data on an author page) and continue processing?
- *Code Quality:* Is your code clean, well-commented, and easy to understand? Did you follow Python/Django conventions?
- *Project Structure & Reusability:* Is your logic well-organized? Is the database logic cleanly separated from the parsing logic?
- *Tool Choice & Rationale:* Did you choose appropriate tools for the job, and can you justify your decisions in your documentation?
