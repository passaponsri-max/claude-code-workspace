"""
csv_cleaner.py — Example: Clean and process a CSV file

USAGE EXAMPLE:
  python examples/csv_cleaner.py

HOW TO USE WITH CLAUDE CODE:
  Tell Claude Code: "Read my sales_data.csv, remove duplicates, 
  fix dates to DD/MM/YYYY, and give me a summary of total revenue per month"
  Claude Code will adapt this script to your specific file and needs.
"""

import pandas as pd
import os
from datetime import datetime

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
INPUT_FILE = "your_data.csv"       # Change this to your actual CSV file
OUTPUT_DIR = "outputs"
OUTPUT_FILE = f"{OUTPUT_DIR}/clean_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# ─── MAIN SCRIPT ───────────────────────────────────────────────────────────────
def clean_csv(input_file):
    """Load, clean, and return a cleaned DataFrame."""
    print(f"Reading file: {input_file}")
    
    try:
        df = pd.read_csv(input_file, encoding="utf-8")
    except FileNotFoundError:
        print(f"ERROR: File not found: {input_file}")
        print("Please put your CSV file in the project folder and update INPUT_FILE above.")
        return None
    except Exception as e:
        print(f"ERROR reading file: {e}")
        return None
    
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    print(f"Columns: {list(df.columns)}")
    
    # ── Step 1: Remove completely empty rows ──
    before = len(df)
    df.dropna(how="all", inplace=True)
    print(f"Removed {before - len(df)} completely empty rows")
    
    # ── Step 2: Remove duplicate rows ──
    before = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Removed {before - len(df)} duplicate rows")
    
    # ── Step 3: Trim whitespace from text columns ──
    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].str.strip()
    print(f"Trimmed whitespace from {len(text_cols)} text columns")
    
    # ── Step 4: Print a summary ──
    print("\n--- Data Summary ---")
    print(df.describe(include="all"))
    
    return df


def save_clean_csv(df, filepath):
    """Save cleaned DataFrame to CSV."""
    if df is None:
        return
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False, encoding="utf-8")
    print(f"\nSaved clean file to: {filepath}")
    print(f"Final size: {len(df)} rows")


if __name__ == "__main__":
    print("=" * 50)
    print("CSV Cleaner — Claude Code Workspace")
    print("=" * 50)
    
    df = clean_csv(INPUT_FILE)
    save_clean_csv(df, OUTPUT_FILE)
    
    print("\nDone!")
