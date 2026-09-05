import csv
from bs4 import BeautifulSoup
import requests

# Target website designed specifically for scraping practice
URL = "https://quotes.toscrape.com/"


def scrape_quotes():
    print("[+] Requesting target website...")
    response = requests.get(URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        data = []
        for q in quotes:
            text = q.find("span", class_="text").text.strip()
            author = q.find("small", class_="author").text.strip()
            data.append([text, author])

        # Save extracted data directly to a CSV spreadsheet
        filename = "scraped_quotes.csv"
        with open(
            filename, "w", newline="", encoding="utf-8"
        ) as csv_file:  #
            writer = csv.writer(csv_file)  #
            writer.writerow(["Quote", "Author"])  # Header
            writer.writerows(data)  # Data rows

        print(
            f"[✓] Success! Extracted {len(data)} items and saved to '{filename}'."
        )
    else:
        print(f"[!] Failed to fetch page. Status code: {response.status_code}")


if __name__ == "__main__":
    scrape_quotes()