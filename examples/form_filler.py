"""
form_filler.py — Example: Automate filling a web form using Playwright

USAGE EXAMPLE:
  # First install playwright browsers (one time):
  playwright install chromium
  
  # Then run:
  python examples/form_filler.py

HOW TO USE WITH CLAUDE CODE:
  Tell Claude Code: "Go to [website URL], fill in the contact form 
  with the data from my_list.csv, and submit it for each row. 
  Save a log of which ones succeeded."
  
  Claude Code will look at the actual website and write the 
  correct selectors and form logic for you.

IMPORTANT: Always review automation scripts before running them.
Only use on websites you own or have permission to automate.
"""

import asyncio
import csv
import os
from datetime import datetime
from playwright.async_api import async_playwright

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
TARGET_URL = "https://www.google.com"   # Change to your target URL
INPUT_FILE = "form_data.csv"            # CSV with data to fill in
LOG_FILE = f"outputs/form_filler_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
HEADLESS = False  # Set True to run invisible (no browser window shown)

# ─── EXAMPLE FORM DATA ─────────────────────────────────────────────────────────
# Replace with your actual CSV file
EXAMPLE_DATA = [
    {"name": "Alice Smith",  "email": "alice@example.com",  "message": "Hello from Alice"},
    {"name": "Bob Jones",    "email": "bob@example.com",    "message": "Hello from Bob"},
]

# ─── MAIN SCRIPT ───────────────────────────────────────────────────────────────
def load_data(filepath):
    """Load form data from CSV, or use examples if file not found."""
    if not os.path.exists(filepath):
        print(f"Note: {filepath} not found. Using example data.")
        return EXAMPLE_DATA
    
    with open(filepath, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def log_result(logfile, row_num, name, status, message=""):
    """Append a result to the log file."""
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    with open(logfile, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%H:%M:%S")
        f.write(f"[{timestamp}] Row {row_num}: {name} — {status} {message}\n")


async def fill_form(page, data):
    """
    Fill and submit the form for one row of data.
    
    NOTE: Claude Code will update this function with the correct 
    selectors for YOUR specific website. These are just examples.
    """
    try:
        # Navigate to the form page
        await page.goto(TARGET_URL, wait_until="networkidle")
        print(f"  Opened: {TARGET_URL}")
        
        # ── Claude Code will replace these with the correct selectors ──
        # Example: fill a text input by its placeholder text
        # await page.fill('input[placeholder="Your Name"]', data["name"])
        # await page.fill('input[type="email"]', data["email"])
        # await page.fill('textarea[name="message"]', data["message"])
        
        # Example: click a submit button
        # await page.click('button[type="submit"]')
        
        # Wait for confirmation
        # await page.wait_for_selector(".success-message", timeout=5000)
        
        print(f"  Successfully filled form for: {data.get('name', 'Unknown')}")
        return True, "Success"
        
    except Exception as e:
        print(f"  Error: {e}")
        return False, str(e)


async def main():
    """Main automation loop."""
    print("=" * 50)
    print("Form Filler — Claude Code Workspace")
    print("=" * 50)
    
    data_rows = load_data(INPUT_FILE)
    print(f"Processing {len(data_rows)} rows...\n")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        context = await browser.new_context()
        page = await context.new_page()
        
        success_count = 0
        
        for i, row in enumerate(data_rows, 1):
            name = row.get("name", f"Row {i}")
            print(f"[{i}/{len(data_rows)}] Processing: {name}")
            
            ok, msg = await fill_form(page, row)
            log_result(LOG_FILE, i, name, "OK" if ok else "FAILED", msg)
            
            if ok:
                success_count += 1
            
            # Small pause between submissions (be polite to servers)
            await asyncio.sleep(1)
        
        await browser.close()
    
    print(f"\nCompleted: {success_count}/{len(data_rows)} successful")
    print(f"Log saved to: {LOG_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
