# Job Application Management System

A simple job application tracking system built with Django framework for learning purposes.

## Overview

This project is a web-based application that helps users track their job application progress. It provides an intuitive interface to manage company information, application deadlines, interview dates, and application status.

## Built With

- **Django 5.1.10** - Python web framework
- **SQLite** - Database (default Django database)
- **HTML/CSS** - Frontend styling
- **Python 3.x** - Backend programming language

## Features

- ✅ Add new job application records
- ✅ Edit company names and notes
- ✅ Update application dates directly from the main interface
- ✅ Track status for each application stage (pass/fail/---)
- ✅ Sort records by creation date, application deadline, or first interview date
- ✅ Delete unwanted records
- ✅ Clean and responsive table-based interface

## Application Stages Tracked

1. **Application Deadline** - When you need to submit your application
2. **Online Test Deadline** - When online assessments are due
3. **First Interview Date** - Scheduled first interview
4. **Second Interview Date** - Scheduled second interview
5. **Notes** - Additional remarks with results tracking

## Project Structure

```
job_management/
├── manage.py                    # Django management script
├── README.md                    # Project documentation
├── db.sqlite3                   # SQLite database file
├── job_management/              # Main project configuration
│   ├── __init__.py
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
└── jobs/                        # Main application
    ├── __init__.py
    ├── admin.py                 # Django admin configuration
    ├── apps.py                  # App configuration
    ├── models.py                # Database models
    ├── views.py                 # View functions
    ├── urls.py                  # App URL patterns
    ├── migrations/              # Database migrations
    │   ├── __init__.py
    │   ├── 0001_initial.py
    │   ├── 0002_remove_jobapplication_application_rejected_and_more.py
    │   └── 0003_rename_notes_status_to_notes_result.py
    └── templates/jobs/          # HTML templates
        ├── base.html            # Base template with CSS
        ├── job_list.html        # Main listing page
        ├── add_job.html         # Add new record form
        └── edit_job.html        # Edit existing record form
```

## Installation & Setup

### Prerequisites

- Python 3.x installed
- pip package manager
- Virtual environment (recommended)

### Installation Steps

1. **Clone or download the project**
   ```bash
   # Navigate to the project directory
   cd job_management
   ```

2. **Create and activate virtual environment** (optional but recommended)
   ```bash
   # Using conda
   conda create -n job_env python=3.x
   conda activate job_env
   
   # Or using venv
   python -m venv job_env
   # On Windows:
   job_env\Scripts\activate
   # On macOS/Linux:
   source job_env/bin/activate
   ```

3. **Install Django**
   ```bash
   pip install django
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser** (optional - for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/ (if superuser created)

## Usage

### Adding New Records
1. Click "添加新记录" (Add New Record) button
2. Enter company name (required) and notes (optional)
3. Save the record

### Managing Dates and Status
- **Dates**: Click on any date field in the main table to select a date
- **Status**: Use dropdown menus below each date to set status (---, pass, fail)
- **Notes Result**: Set the overall result for the notes section

### Editing Records
- Click "编辑" (Edit) button to modify company name and notes
- Date modifications are done directly from the main interface

### Sorting Records
Use the sorting links at the top:
- **默认** (Default): Sort by creation date
- **投递截至日期** (Application Deadline): Sort by application deadline
- **一面日期** (First Interview Date): Sort by first interview date

## Database Model

The `JobApplication` model includes:

- `company_name` - Company name (CharField, required)
- `application_deadline` - Application deadline (DateField, optional)
- `online_test_deadline` - Online test deadline (DateField, optional)
- `first_interview_date` - First interview date (DateField, optional)
- `second_interview_date` - Second interview date (DateField, optional)
- `notes` - Additional notes (TextField, max 100 characters)
- `application_status` - Application status (CharField: ---, pass, fail)
- `online_test_status` - Online test status (CharField: ---, pass, fail)
- `first_interview_status` - First interview status (CharField: ---, pass, fail)
- `second_interview_status` - Second interview status (CharField: ---, pass, fail)
- `notes_result` - Notes result (CharField: ---, pass, fail)
- `created_at` - Record creation timestamp
- `updated_at` - Record last update timestamp

## Learning Purpose

This project was built as a learning exercise to understand:
- Django framework fundamentals
- Model-View-Template (MVT) architecture
- Database operations with Django ORM
- Form handling and validation
- Template rendering and CSS styling
- URL routing and view functions

## License

This project is for educational purposes only.

## Contributing

This is a learning project. Feel free to fork and experiment with the code for your own educational purposes.

## Contact

This project was created as part of Django framework learning and practice.
