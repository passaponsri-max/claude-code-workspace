# Claude Code Workspace

> A ready-to-use workspace for running Claude Code — Anthropic's AI coding assistant that works directly in your terminal.

---

## What is Claude Code?

Claude Code is a command-line tool that lets you work with Claude (the AI) directly inside your project folders. Unlike a chat window, Claude Code can:

- Read and write your actual files
- Run terminal commands for you
- Understand your entire project at once
- Remember your preferences (via CLAUDE.md)
- Build scripts, tools, and automations end-to-end

---

## Quick Start (First Time Setup)

### Step 1: Install Node.js
Download and install from: https://nodejs.org (choose the LTS version)

### Step 2: Install Claude Code
Open your terminal and run:
```bash
npm install -g @anthropic-ai/claude-code
```

### Step 3: Get Your Anthropic API Key
1. Go to https://console.anthropic.com
2. Sign in or create an account
3. Click "API Keys" and create a new key
4. Copy it (you only see it once!)

### Step 4: Set Your API Key
```bash
# On Mac/Linux:
export ANTHROPIC_API_KEY=sk-ant-your-key-here

# On Windows (Command Prompt):
set ANTHROPIC_API_KEY=sk-ant-your-key-here

# On Windows (PowerShell):
$env:ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

### Step 5: Clone This Workspace
```bash
git clone https://github.com/passaponsri-max/claude-code-workspace.git
cd claude-code-workspace
```

### Step 6: Start Claude Code!
```bash
claude
```

That's it! Claude Code will automatically read the CLAUDE.md file and know your preferences.

---

## How to Use Claude Code (Daily Use)

Just open your terminal, navigate to this folder, type `claude`, and then describe what you want in plain English. Examples:

```
> Scrape the product listings from this URL and save them to a CSV file
> Read my sales_data.csv and tell me the top 5 products by revenue
> Write a script that checks a list of URLs and tells me which ones are broken
> Draft a professional follow-up email for a client meeting about [topic]
> Build me a simple dashboard that shows data from my CSV file
```

---

## Real-World Examples for This Workspace

### Example 1: Web Research & Summarization
**What you say:**
```
Research the topic "sustainable packaging trends 2025", 
visit the top 5 search results, and write me a summary 
report saved to outputs/packaging_trends_report.md
```
**What Claude Code does:** Searches the web, reads the pages, writes a report, saves it — all automatically.

---

### Example 2: Clean Up a Messy CSV File
**What you say:**
```
Read the file messy_data.csv, remove duplicate rows, 
fix the date format to DD/MM/YYYY, and save the 
clean version to outputs/clean_data.csv
```
**What Claude Code does:** Writes a Python script, runs it, and gives you a clean file.

---

### Example 3: Automate a Web Form
**What you say:**
```
Write a Playwright script that goes to [website URL], 
fills in the contact form with the data from contacts.csv, 
and submits it for each row
```
**What Claude Code does:** Builds a browser automation script you can run anytime.

---

### Example 4: Draft Multiple Emails at Once
**What you say:**
```
I have a list of 20 clients in clients.csv. 
Draft a personalized follow-up email for each one 
using their name, company, and last meeting date. 
Save each email as a separate .txt file in outputs/emails/
```
**What Claude Code does:** Reads the CSV, writes 20 personalized emails, saves them all.

---

### Example 5: Monitor a Website for Changes
**What you say:**
```
Write a script that checks [website URL] every hour 
and sends me an alert (saves to a log file) 
if the price changes from what it is now
```
**What Claude Code does:** Builds a monitoring script that runs on a schedule.

---

### Example 6: Build a Simple Internal Tool
**What you say:**
```
Build me a simple web page where I can upload a CSV file 
and it shows me the data as a table with filters and sorting
```
**What Claude Code does:** Builds a working HTML+JavaScript tool you can open in your browser.

---

### Example 7: API Data Fetching
**What you say:**
```
Connect to the OpenWeatherMap API and fetch the 7-day 
forecast for Bangkok, Thailand. Save it as a nicely 
formatted report in outputs/weather_report.txt
```
**What Claude Code does:** Writes the API integration code, tests it, and saves the results.

---

## Folder Structure

```
claude-code-workspace/
├── CLAUDE.md              <- Claude Code reads this automatically (your preferences)
├── README.md              <- This file
├── .gitignore             <- Keeps secrets out of GitHub
├── requirements.txt       <- Python packages to install
├── examples/              <- Ready-to-run example scripts
│   ├── web_scraper.py
│   ├── research_summary.py
│   ├── csv_cleaner.py
│   ├── form_filler.py
│   └── email_drafter.py
├── outputs/               <- All outputs go here (add your own!)
└── projects/              <- Put your actual work projects here
```

---

## Install Python Packages

```bash
pip install -r requirements.txt
```

---

## Tips for Getting the Best Results

- **Be specific** — instead of "analyze my data", say "read sales.csv and calculate the monthly total revenue for each product category"
- **Mention the output format** — "save as CSV", "save as a PDF report", "print a table"
- **Iterate** — if the result isn't quite right, just say "change X to Y" and Claude Code will update it
- **Ask for explanations** — "explain what this script does line by line" is totally valid
- **CLAUDE.md is your friend** — edit it anytime to add new preferences or context

---

## Useful Claude Code Commands

| Command | What it does |
|---|---|
| `claude` | Start an interactive session |
| `claude "do this task"` | Run a one-off task without interactive mode |
| `claude --help` | See all options |
| `/exit` or Ctrl+C | Exit Claude Code |
| `/clear` | Clear the conversation history |

---

## Resources

- Official docs: https://docs.anthropic.com/claude-code
- API Console: https://console.anthropic.com
- Anthropic: https://anthropic.com

---

*Built with Claude — by passaponsri-max*
