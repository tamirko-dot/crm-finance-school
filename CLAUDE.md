# CLAUDE.md — CRM Finance School

## Project Context

LMS for training credit analysts in real estate financing, Israel. 25 users, 12 courses in "Real Estate Finance" domain.
Django 5.1 + Supabase PostgreSQL + Railway hosting. All UI is Hebrew RTL. Built by Tamir Kochavi.

## Conda Environment — Check First

The conda env for this project is `Financing_education_3_11` (Python 3.11).

**At the start of every session, verify the env is active:**
```bash
python --version        # expect 3.11.x
which python            # expect .../envs/Financing_education_3_11/...
echo $CONDA_DEFAULT_ENV # expect Financing_education_3_11
```

If wrong: STOP and ask Tamir to activate the correct env. Never create, switch, or recreate envs.
Never use `venv`, `virtualenv`, or `conda install` for project deps — use `pip` only.

## Timezone — Critical

```python
TIME_ZONE = 'Asia/Jerusalem'
USE_TZ = True
```

All cooldown calculations (24h, 72h between exam retries) are **wall-clock Israel time**.
Never compute cooldowns in UTC and compare to local time — always use `django.utils.timezone.now()`.

## Tech Stack

- **Backend:** Django 5.1, Python 3.11
- **Database:** Supabase (managed PostgreSQL) via `DATABASE_URL`
- **Auth:** Django auth for sessions; Supabase Auth for credential validation
- **Frontend:** Django templates + Tailwind CSS via CDN + Alpine.js (if needed)
- **State machines:** `django-fsm` — all lifecycle statuses use FSM transitions
- **Storage:** `core/services/storage.py` — never call Supabase Storage SDK directly from views
- **Email:** `core/services/email.py` — stub only in MVP; writes Notification rows
- **Hosting:** Railway via GitHub integration

## Directory Structure

```
crm_finance_school/   Django project config
  settings/
    base.py           shared settings
    dev.py            local dev (used by manage.py)
    prod.py           production (used by wsgi.py)
core/
  middleware/rtl.py   sets Content-Language: he, injects direction into context
  services/storage.py StorageService abstraction (wraps Supabase Storage)
  services/email.py   EmailService stub (writes Notification rows, logs)
  decorators/roles.py @trainee_required, @manager_required, etc.
accounts/             Custom User model, login/logout views
content/              Domain, Course, Module, ModuleComponent, Question, QuestionOption
enrollment/           CourseEnrollment (FSM), UnlockRequest (FSM), ModuleProgress
exams/                ExamAttempt (FSM), ExamAttemptQuestion (snapshots)
capstone/             CapstoneSubmission, CapstoneRubricScore
documents/            LearningDocument, DocumentTag, Notification, AuditLog
reports/              Manager/CEO reporting views
templates/            All HTML templates (base.html is the master)
static/               CSS, JS assets
```

## Coding Standards

- PEP 8 + Black (line length 100) + Ruff linting
- Type hints on all function signatures
- Models in English, field names in English snake_case
- UI strings in Hebrew via `gettext_lazy`
- Class-based views where they simplify; function views otherwise
- Always `select_related` / `prefetch_related` to avoid N+1

## Status Machines (django-fsm)

All entity lifecycles use FSM transitions — **never assign `.status` directly**:

| Model | States |
|---|---|
| `CourseEnrollment` | locked → requested → open → in_progress → passed/failed |
| `UnlockRequest` | pending → approved/denied |
| `ExamAttempt` | in_progress → submitted → graded |
| `CapstoneSubmission` | submitted → under_review → passed/failed |

Transitions go through named methods: `enrollment.approve_unlock()`, `attempt.submit()`, etc.

## Exam Snapshot Mechanism (Non-Negotiable)

When an `ExamAttempt` starts, every question is snapshotted into `ExamAttemptQuestion`:
- `stem_html_snapshot`, `options_snapshot_json`, `correct_option_index_snapshot`
- `senior_insight_snapshot_he`, `explanation_snapshot_html_he`
- `question_version_at_attempt` (the `Question.version` at attempt start)

Grading always uses the snapshot. If an admin edits a question mid-exam, the trainee continues
to see and be graded against the snapshot. The live `Question` table is for authoring only.

## URL Slugs — No Numeric IDs in URLs

Courses, modules, and documents use `slug` fields in URLs.
Never expose numeric PKs in user-facing URLs (IDOR prevention).

## Security Rules

- Django ORM only — no raw SQL
- Server-side validation on every form
- File uploads: validate type (`.docx` only for capstone), size (≤25MB), content-type
- Never log passwords or PII
- CSRF on all forms

## Adding Content (No Code Changes)

Adding a new course or domain is a **data operation only**:
1. Insert a `Domain` row (if new domain)
2. Insert `Course` rows with `phase`, `course_number`, `passing_score_pct`
3. Insert `Module` rows
4. Insert `ModuleComponent` rows (reading, comprehension, exercises, summary)
5. Insert `Question` and `QuestionOption` rows

Or use: `python manage.py import_questions <file>` / `python manage.py import_documents <file>`

## Common Commands

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py import_questions path/to/file.json
python manage.py import_documents path/to/file.json
pytest
black .
ruff check .
```

## Out of Scope for MVP

- Mobile responsive design
- Multi-language UI (Hebrew only)
- Real-time features (websockets, live notifications)
- Sophisticated analytics dashboards
- Question bank calibration analytics (capture data only)
- Plagiarism detection on capstone uploads
- SSO / OAuth
- Payment / billing
- Public marketing pages
- Capstone Auto-Draft Generator (Phase 7 stretch — document in phase if skipped)

## Do NOT

- Use raw SQL (use Django ORM)
- Bypass RBAC decorators
- Assign `.status` directly on FSM models
- Call Supabase Storage SDK from views or models (use `StorageService`)
- Install packages outside the conda env
- Expose numeric PKs in user-facing URLs
- Use `|safe` in templates without careful XSS review
