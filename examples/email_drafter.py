"""
email_drafter.py — Example: Draft personalized emails from a contact list

USAGE EXAMPLE:
  python examples/email_drafter.py

HOW TO USE WITH CLAUDE CODE:
  Tell Claude Code: "I have a contacts.csv with columns: name, company, last_meeting_date.
  Draft a personalized follow-up email for each contact and save them to outputs/emails/"
  
  Claude Code will read your actual CSV and write emails tailored to each person.
"""

import csv
import os
from datetime import datetime

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
INPUT_FILE = "contacts.csv"       # Your contacts CSV file
OUTPUT_DIR = "outputs/emails"     # Where to save the email drafts

# ─── EMAIL TEMPLATE ──────────────────────────────────────────────────────────
# Claude Code can rewrite this template for any purpose
EMAIL_TEMPLATE = """Subject: Following up — {topic}

Dear {name},

I hope this message finds you well.

I wanted to follow up on our recent conversation about {topic}. 
It was great connecting with you at {company}, and I wanted to 
share a few thoughts since our last meeting.

{custom_message}

Please feel free to reach out if you have any questions or if 
you would like to schedule a follow-up call.

Best regards,
[Your Name]
[Your Contact Info]
"""

# ─── EXAMPLE CONTACTS ─────────────────────────────────────────────────────────
# This is example data — replace contacts.csv with your real file
EXAMPLE_CONTACTS = [
    {"name": "Sarah Johnson", "company": "Acme Corp", "topic": "the Q1 partnership proposal", "custom_message": "I believe there are exciting synergies we can explore together."},
    {"name": "Mark Lee",      "company": "TechStart",  "topic": "our software integration discussion", "custom_message": "The demo we discussed could be ready by next week."},
    {"name": "Priya Patel",   "company": "GlobalTrade","topic": "the logistics optimization project", "custom_message": "I have prepared some data that might be useful for your team."},
]

# ─── MAIN SCRIPT ───────────────────────────────────────────────────────────────
def load_contacts(filepath):
    """Load contacts from CSV file."""
    if not os.path.exists(filepath):
        print(f"Note: {filepath} not found. Using example contacts instead.")
        return EXAMPLE_CONTACTS
    
    contacts = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            contacts.append(row)
    
    print(f"Loaded {len(contacts)} contacts from {filepath}")
    return contacts


def draft_email(contact, template):
    """Fill in the email template for one contact."""
    try:
        return template.format(**contact)
    except KeyError as e:
        print(f"  Warning: Missing field {e} for {contact.get('name', 'Unknown')}")
        return template


def save_emails(contacts, template, output_dir):
    """Draft and save one email per contact."""
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\nDrafting emails for {len(contacts)} contacts...")
    
    for i, contact in enumerate(contacts, 1):
        name = contact.get("name", f"Contact_{i}")
        safe_name = name.replace(" ", "_").replace("/", "-")
        
        email_text = draft_email(contact, template)
        filepath = os.path.join(output_dir, f"email_{i:02d}_{safe_name}.txt")
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(email_text)
        
        print(f"  [{i}] Saved email for {name} → {filepath}")
    
    print(f"\nAll {len(contacts)} emails saved to: {output_dir}/")


if __name__ == "__main__":
    print("=" * 50)
    print("Email Drafter — Claude Code Workspace")
    print("=" * 50)
    
    contacts = load_contacts(INPUT_FILE)
    save_emails(contacts, EMAIL_TEMPLATE, OUTPUT_DIR)
    
    print("\nDone! Review emails in the outputs/emails/ folder before sending.")
