"""
web_scraper.py — Example: Scrape a website and save results to CSV

USAGE EXAMPLE:
  python examples/web_scraper.py

HOW TO USE WITH CLAUDE CODE:
  Tell Claude Code: "Scrape all product names and prices from [URL] and save to outputs/products.csv"
  Claude Code will modify this script or write a new one based on your specific website.
"""

import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
URL = "https://books.toscrape.com"   # Change this to your target URL
OUTPUT_DIR = "outputs"
OUTPUT_FILE = f"{OUTPUT_DIR}/scraped_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# ─── MAIN SCRIPT ───────────────────────────────────────────────────────────────
def scrape_website(url):
    """Fetch and parse a webpage, return list of items."""
    print(f"Fetching: {url}")
    
    try:
        # Send request with a browser-like header
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error if request failed
        print(f"Success! Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return []
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, "lxml")
    
    # ── EXAMPLE: Extract book titles and prices from books.toscrape.com ──
    # Claude Code will change this section for your specific website
    items = []
    products = soup.select("article.product_pod")
    
    print(f"Found {len(products)} items on the page...")
    
    for i, product in enumerate(products, 1):
        title = product.select_one("h3 a")["title"] if product.select_one("h3 a") else "N/A"
        price = product.select_one(".price_color").text.strip() if product.select_one(".price_color") else "N/A"
        rating = product.select_one("p.star-rating")["class"][1] if product.select_one("p.star-rating") else "N/A"
        
        items.append({
            "title": title,
            "price": price,
            "rating": rating,
        })
        print(f"  [{i}] {title} — {price}")
    
    return items


def save_to_csv(items, filepath):
    """Save list of dicts to a CSV file."""
    if not items:
        print("No items to save.")
        return
    
    # Create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=items[0].keys())
        writer.writeheader()
        writer.writerows(items)
    
    print(f"\nSaved {len(items)} items to: {filepath}")


if __name__ == "__main__":
    print("=" * 50)
    print("Web Scraper — Claude Code Workspace")
    print("=" * 50)
    
    data = scrape_website(URL)
    save_to_csv(data, OUTPUT_FILE)
    
    print("\nDone!")
