# Notes Management App

A Django-based notes management app for creating, editing, searching, and organizing personal notes by category. The app includes user authentication, a clean dashboard, category filters, and a recently updated notes section.

## Features

- User registration and login
- Create, edit, and delete notes
- Search notes by title
- Filter notes by category
- View recently updated notes
- Responsive HTML and CSS interface
- SQLite database for local development

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- WhiteNoise
- Gunicorn

## Project Structure

```text
Notes/
├── Notes/              # Django project settings
├── notes_app/          # Main notes application
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aloshitom10/Notes-Management-App.git
cd Notes-Management-App
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Usage

Register a new account, log in, and start creating notes. Notes can be categorized as Personal, Study, Work, or Important. The dashboard lets you search, filter, edit, and delete notes from one place.

## Deployment

Live app:

```text
https://notes-app-1-luwa.onrender.com
```

## Repository Topics

```text
django notes-app crud auth sqlite
```
