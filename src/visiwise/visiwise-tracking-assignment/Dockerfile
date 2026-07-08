FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7000

CMD ["sh", "-c", "touch db.sqlite3 && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
