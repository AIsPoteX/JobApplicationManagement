# Job Application Management System

A simple job application tracking system built with Django framework for learning purposes.

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

This is a learning project.

## :exclamation: What's the next? :exclamation:
+ Add the ability to increase/decrease the number of interviews.

## Gemini integration

1. Install the SDK: `pip install google-generativeai`
2. Export your API key before starting the server:
	- macOS/Linux: `export GEMINI_API_KEY="your-key"`
	- Windows (cmd): `set GEMINI_API_KEY=your-key`
3. Call the endpoint (POST): `/company-brief/` with form data `company_name=Acme Co` to receive a JSON brief.

## Thanks
+ Thanks to the MDN open-source project for its tutorials. (https://github.com/mdn/django-locallibrary-tutorial.git)
+ Thanks to Mr. "Google AI Studio" for its patient guidance.
+ Thanks to Mr. "Github Copilot" for its assistive guidance.
