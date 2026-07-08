# Quotes Scraper

A Django-based web scraper that extracts quotes and author information from the "Quotes to Scrape" website.

## Assignment

See [interview-assignment.md](interview-assignment.md) for the complete assignment requirements and specifications.

## Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional, for containerized setup)

## Setup

### Option 1: Using Docker (Recommended)

1. Clone the repository and navigate to the project directory
2. Run the application:
   ```bash
   docker-compose up --build
   ```
3. The Django development server will be available at `http://localhost:8000`

### Option 2: Manual Setup

1. Clone the repository and navigate to the project directory
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. The Django development server will be available at `http://localhost:127.0.0.1:8000`
