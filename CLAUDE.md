# CLAUDE.md — Claude Code Configuration

This file tells Claude Code about this project, your preferences, and how to work with you.
Claude Code reads this file automatically every time you start a session in this folder.

---

## About This Workspace

**Owner:** passaponsri-max  
**Purpose:** A personal Claude Code workspace for web automation, research, data processing, document drafting, and scripting tasks.  
**Primary language:** Python 3.x  
**Key tools used:** requests, playwright, pandas, openpyxl, beautifulsoup4

---

## My Preferences

- Write clean, readable code with comments explaining what each section does
- Always print progress so I can see what the script is doing (e.g. "Fetching page 1 of 5...")
- Save all output to the outputs/ folder
- When writing scripts, include a short usage example at the top as a comment
- Prefer simple solutions over complex ones — I am not a professional developer
- If something could go wrong, add try/except error handling
- Use requirements.txt to list dependencies for every project

---

## Folder Structure

claude-code-workspace/
  CLAUDE.md              <- This file (Claude Code reads it automatically)
  README.md              <- How to install and use Claude Code
  .gitignore             <- Keeps secrets and temp files out of GitHub
  requirements.txt       <- Python packages needed
  examples/              <- Ready-to-run example scripts
    web_scraper.py         Example: scrape a website and save results
    research_summary.py    Example: fetch URLs and summarize content  
    csv_cleaner.py         Example: clean and process a CSV file
    form_filler.py         Example: automate filling a web form
    email_drafter.py       Example: draft emails from a template
  outputs/               <- All script outputs go here (auto-created)
  projects/              <- Your actual work projects go here

---

## Common Tasks & How to Ask Claude Code

Web Research:
"Research [topic], visit these 5 URLs, and write me a summary report saved as outputs/report.md"

Data Processing:
"Read the file data.csv, clean it up, remove duplicates, and save a clean version to outputs/"

Web Automation:
"Write a Playwright script that goes to [website], logs in, and downloads the latest report"

Document Drafting:
"Draft a professional email to [person] about [topic] and save it to outputs/email_draft.txt"

API Integration:
"Write a script that calls the [API name] API and saves the results to a JSON file"

---

## How to Start Claude Code

# Install Claude Code (one time only)
npm install -g @anthropic-ai/claude-code

# Set your API key (one time only - get it from console.anthropic.com)
export ANTHROPIC_API_KEY=your_api_key_here

# Navigate to this workspace
cd claude-code-workspace

# Start Claude Code - it will read this CLAUDE.md automatically!
claude

---

## Notes for Claude Code

- Always ask before making permanent changes to files I have not mentioned
- If you are unsure about something, ask me rather than guessing
- Keep scripts modular: one script = one task
- Never hardcode API keys or passwords in scripts; use environment variables instead
- When a task is done, tell me exactly what files were created and where they are
