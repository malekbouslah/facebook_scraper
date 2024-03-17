# FastAPI Facebook Scraper

This project is a FastAPI application that scrapes data from Facebook pages and saves it to a MySQL database.

## Running the Application

1. Clone this repository:

```bash
git clone https://github.com/malekbouslah/facebook_scraper.git
cd facebook_scraper
```
2. Build and run the Docker containers:
```bash
docker-compose up --build -d
```
The FastAPI service will be available at http://localhost:8000

## Running the Test
```bash
pytest test.py
```
Using postamn:
http://localhost:8000/scrape/{page_name}
