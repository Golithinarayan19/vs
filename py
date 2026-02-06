import requests
from bs4 import BeautifulSoup
import csv

# Target website (scrape-friendly)
URL = "https://books.toscrape.com/"

# Send GET request
response = requests.get(URL)

# Check if request was successful
if response.status_code != 200:
    print("Failed to fetch the webpage")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all book containers
books = soup.find_all("article", class_="product_pod")

# Prepare CSV file
with open("books_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability", "Link"])

    for book in books:
        # Safely extract title
        title_tag = book.find("h3")
        title = title_tag.a["title"] if title_tag else "N/A"

        # Safely extract price
        price_tag = book.find("p", class_="price_color")
        price = price_tag.text if price_tag else "N/A"

        # Safely extract availability
        availability_tag = book.find("p", class_="instock availability")
        availability = availability_tag.text.strip() if availability_tag else "N/A"

        # Safely extract link
        link_tag = book.find("a")
        link = URL + link_tag["href"] if link_tag else "N/A"

        # Write row to CSV
        writer.writerow([title, price, availability, link])

print("✅ Data scraped successfully and saved to books_data.csv")
