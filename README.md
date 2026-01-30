# Job Application Management System

## What it is

This is a specialized web application designed to navigate the high-intensity Japanese Job Hunting process (Shuukatsu). It serves as a centralized intelligence hub for candidates managing dozens of concurrent applications. Furthermore, by leveraging the Google Gemini API, the system allows users to generate comprehensive company briefs and tailored interview talking points simply by entering a company name.

## Why I built it?

Baseing on my Economics background in resource optimization, I developed this Django system with a product-first mindset to streamline the complex Japanese job-hunting workflow. By integrating the Gemini API, I solved problems through AI-driven automation.

## How it solves problems.

+ Consolidates application deadlines, interview stages, and complex corporate data into a single, manageable interface to prevent critical oversights.
+ Automates the "Enterprise Research" (Kigyo Kenkyu) phase, which is traditionally time-consuming and manual.
+ Provides a unified repository for interview transcripts (PDFs) and AI-generated briefs to ensure consistency across multiple interview rounds.


## Built With

- **Django 5.1.10** - Python web framework
- **SQLite** - Database (default Django database)
- **HTML** - Frontend styling
- **Python 3.x** - Backend programming language

## Features

- ✅ Add new job application records
- ✅ Edit company names and notes
- ✅ Update application dates directly from the main interface
- ✅ Track status for each application stage (pass/fail/---)
- ✅ Sort records by creation date, application deadline, or first interview date
- ✅ Delete unwanted records
- ✅ Clean and responsive table-based interface
- ✅ Upload interview transcript PDF files.
- ✅ Generate a Gemini-backed company brief for interview prep

## :exclamation: What's the next? :exclamation:
+ Make AI-generated briefs saved in the "Memo" as .md files.
+ use Docker to containerize the application.

## Gemini integration

1. Install the SDK: `pip install google-generativeai`
2. Export your API key before starting the server:
	- Windows (cmd): `set GEMINI_API_KEY=your-key`
3. Call the endpoint (POST): `/company-brief/` with form data `company_name=Acme Co` to receive a JSON brief.

## Thanks
+ Thanks to the MDN open-source project for its tutorials. (https://github.com/mdn/django-locallibrary-tutorial.git)
+ Thanks to Mr. "Google AI Studio" for its patient guidance.
+ Thanks to Mr. "Github Copilot" for its assistive guidance.
