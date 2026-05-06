# CRM Finance School — LMS for Real Estate Credit Analysts

A Learning Management System for training credit analysts in a non-bank real estate financing company in Israel.
25 users, 12 courses, Hebrew RTL UI, Django 5 + Supabase + Railway.

## Prerequisites

The developer must create and activate their conda environment **before** running any commands:

```bash
conda create -n Financing_education_3_11 python=3.11 -y
conda activate Financing_education_3_11
```

## Setup

```bash
# Install dependencies into the active conda env
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Configure environment
cp .env.example .env
# Edit .env — fill in DJANGO_SECRET_KEY, DATABASE_URL, and Supabase keys

# Database
python manage.py migrate
python manage.py createsuperuser

# Run locally
python manage.py runserver
```

## Environment Variables

| Variable | Description |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key (generate with `python -c "import secrets; print(secrets.token_urlsafe(50))"`) |
| `DJANGO_DEBUG` | `True` for dev, `False` for prod |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hosts |
| `DATABASE_URL` | Supabase PostgreSQL connection string |
| `SUPABASE_URL` | Your Supabase project URL |
| `SUPABASE_ANON_KEY` | Supabase anon/public key |
| `SUPABASE_SERVICE_KEY` | Supabase service role key (server-side only) |
| `SUPABASE_STORAGE_BUCKET` | Storage bucket name (e.g. `learning-materials`) |
| `EMAIL_BACKEND` | Use `dummy.EmailBackend` for MVP |

## Supabase Setup

1. Create a new Supabase project at supabase.com
2. Copy the project URL and both API keys into `.env`
3. Create a storage bucket named `learning-materials` (public read, authenticated write)
4. Use the connection string from Project Settings → Database → Connection string (URI) as `DATABASE_URL`

## Management Commands

```bash
# Import questions from CSV or JSON
python manage.py import_questions path/to/questions.json

# Import learning documents
python manage.py import_documents path/to/documents.json
```

## Deploy to Railway

1. Push code to GitHub
2. In Railway: New Project → Deploy from GitHub repo
3. Set all env vars from `.env.example` in Railway dashboard (Settings → Variables)
4. Railway will auto-build and deploy
5. Run migrations via Railway shell: `python manage.py migrate`

## Settings

Settings are split by environment:
- `crm_finance_school/settings/base.py` — shared
- `crm_finance_school/settings/dev.py` — local development (`manage.py` uses this)
- `crm_finance_school/settings/prod.py` — production (`wsgi.py` uses this)

## Apps

| App | Purpose |
|---|---|
| `core` | Base views, middleware, services, decorators |
| `accounts` | Custom User model, login/logout |
| `content` | Domain, Course, Module, ModuleComponent, Question |
| `enrollment` | CourseEnrollment, UnlockRequest, ModuleProgress |
| `exams` | ExamAttempt, ExamAttemptQuestion (snapshots) |
| `capstone` | CapstoneSubmission, CapstoneRubricScore |
| `documents` | LearningDocument, DocumentTag, Notification |
| `reports` | Reporting views for managers and CEO |
