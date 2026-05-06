# CRM Finance School — Build Specification

## Role and Mission

You are a senior full-stack engineer building a Learning Management System (LMS) for a non-bank real estate financing company in Israel. The system trains credit analysts through a structured 12-course program. Your task is to build a production-ready MVP that 25 users will actively use.

You are working through Cursor with Claude Code in the terminal. The user (Tamir) is a developer and will review your work iteratively.

## Reference Documents

Two reference documents exist in the project root and define WHAT this system must support:

1. **`curriculum_specification_v2.html`** — Full curriculum specification: 12 courses, 5 phases, module architecture (5 components per module), exam structure, retry management, question bank format, capstone deliverable rubric. Read this fully before writing any code. The system you build must accommodate every structural element described there.

2. **`sample_module_C01M04.html`** — A fully realized sample module showing exactly what the final product looks like to an end-user: reading → comprehension check → graded exercises → summary → glossary. Use this to calibrate the data model and UI.

These documents are in Hebrew. Read them and treat them as authoritative for content structure and pedagogical requirements.

---

## Project Overview

**Domain.** Real estate project finance training, in Israel. The first content domain is "Real Estate Finance" with 12 courses. The system MUST be designed so future content domains (e.g., "Commercial Banking", "Insurance Underwriting") can be added with no architectural change — only content data.

**User base.** 25 users total:
- **20 trainee analysts** — learners
- **3 customer managers** — review capstone deliverables, monitor learner progress, view group reports, approve course unlock requests
- **1 admin** — system administrator who manages content (courses, modules, questions, documents) and users
- **1 CEO** — full read access including all reports

**Language.** Hebrew (RTL) for all UI shown to users. Code, comments, commits, variable names, and database fields in English.

**Platform.** Desktop-only web app. No mobile/tablet support required for MVP.

---

## Tech Stack — Required

| Layer | Technology | Notes |
|---|---|---|
| Environment | **Conda env (pre-created by user)** | The user creates and activates the conda environment BEFORE the session starts. You will receive an already-active environment. Your job is to install dependencies via `pip` *into that active environment*. Do NOT create the env yourself. Do NOT install globally. Do NOT switch to venv. |
| Backend | **Python 3.11+ with Django 5.x** | Use Django everywhere — admin panel comes free, ORM is mature, perfect for 25 users |
| Database | **Supabase (managed PostgreSQL)** | Use Supabase project URL via Django settings |
| Auth | **Supabase Auth** for username+password | Custom Django user model that maps to Supabase user ID |
| Frontend | **Django templates + HTML + Tailwind CSS via CDN** | No SPA. Server-rendered, sprinkle Alpine.js if needed for interactivity. Keep it simple. |
| Hosting | **Railway** | Deploy via GitHub integration |
| Version control | **GitHub** | Initialize repo, set up `.gitignore` properly |
| IDE context | **Cursor** | Authored via Claude Code in Cursor terminal |
| File uploads | Supabase Storage | For capstone Word docs and learning material PDFs |
| Email (future) | Stub interface only | Wire up an `EmailService` class that no-ops in MVP, ready for SendGrid/Resend later |

**Do not propose alternatives.** If you encounter a problem with a chosen technology, document it and ask the user — do not switch silently.

---

## Architectural Principles

1. **Content-as-data.** Course structure is stored in the database, not hardcoded. Adding a new course or domain is a data operation, not a code change.

2. **Domain-agnostic core.** Everything in the system should reference a `Domain` (top-level container). The first domain is "Real Estate Finance — Israel" but the platform must trivially support more.

3. **Role-based access control (RBAC).** Permissions enforced server-side via Django decorators/mixins. Never rely on UI hiding alone.

4. **Audit-first.** Every meaningful state change (course unlocked, exam started, exam submitted, deliverable graded, question updated) writes a row to an `audit_log` table.

5. **Separation of identity and authorization.** Supabase handles "who is this person and is their password right". Django handles "what can they do". Map cleanly.

6. **Pedagogical fidelity.** Adhere strictly to the spec doc on exam mechanics: forward-only navigation, randomized question order per attempt, immediate scoring on submit, distractor explanations stored with each question.

7. **No silent magic.** Every cron-like or scheduled behavior must be either a Django management command runnable manually, or clearly documented.

8. **State machines, not enums.** Every entity that has a lifecycle (`CourseEnrollment.status`, `UnlockRequest.status`, `ExamAttempt.status`, `CapstoneSubmission.status`) MUST use a state machine library (use `django-fsm` or equivalent). Direct field assignment to status is forbidden — transitions go through named methods (`enrollment.unlock()`, `attempt.submit()`, etc.) that enforce preconditions, cooldowns, and side effects (audit log writes, notification stubs). This prevents illegal status jumps and centralizes business logic.

9. **Storage is abstracted.** Do NOT call Supabase Storage SDK directly from views or models. Build a `StorageService` interface in `core/services/storage.py` with methods `upload(file, key)`, `get_url(key)`, `delete(key)`, `list(prefix)`. The MVP implementation wraps Supabase Storage. Future migration to S3/Azure (common requirement in Israeli financial institutions for regulatory reasons) is a single-file swap with no model or view changes.

10. **Question immutability per attempt.** When a trainee starts an exam, the exact text of every question and every option is **snapshotted** into `ExamAttemptQuestion`. If an admin edits a question mid-exam, the trainee continues to see the version that existed at attempt start, and grading uses that snapshot. The live `Question` table is for content authoring; the snapshots are the authoritative record of what was actually answered.

11. **Slug-based URLs, never expose primary keys.** Courses, modules, and learning documents have `slug` fields used in URLs (`/courses/yesodot-mimun/modules/4-ltv-dscr/`). Never accept or emit numeric IDs in URLs visible to users. This prevents Insecure Direct Object Reference (IDOR) — a trainee cannot guess the URL of a locked course by incrementing a number.

12. **Israel-locked timezone.** Set `TIME_ZONE = 'Asia/Jerusalem'`, `USE_TZ = True` in Django settings. All cooldown calculations (24h, 72h between exam retries) are wall-clock relative to Israel local time. Document this explicitly in `CLAUDE.md`.

---

## Visual Design & UI Standards

The system serves a professional, educational, office-style context. Visual tone: **calm, light, restrained, serious without being austere**. Reference: the existing `sample_module_C01M04.html` and the curriculum specification — match their visual vocabulary across every screen.

### Color Palette (use exactly these values)

| Purpose | Hex | Usage |
|---|---|---|
| Page background | `#f5f5f0` | Body of every page (warm cream) |
| Content card | `#ffffff` | Inside containers — primary reading surface |
| Primary | `#1a2638` | Headers, borders, primary buttons, navigation |
| Secondary | `#2c3e50` | Sub-headers, secondary borders, default body text |
| Accent | `#f1c40f` | Highlight badges, progress fills, important pills |
| Muted text | `#6b7280` | Meta info, breadcrumbs, timestamps, helper text |
| Subtle border | `#cbd5e0` | Dividers, table borders, card outlines |
| Even-row stripe | `#f7fafc` | Alternating table rows |
| Field highlight | `#fff8d6` | Inline keyword highlight (think: yellow marker) |

### Soft Callout Backgrounds (for informational boxes)

| Type | Background | Border |
|---|---|---|
| Example / illustration | `#f0f7ff` | `#1976d2` |
| Warning / risk note | `#fff8e1` | `#f57c00` |
| "From the field" / practitioner note | `#e8f5e9` | `#2e7d32` |
| Rule / principle | `#f3e5f5` | `#7b1fa2` |

### Status Colors (badges, pills, indicators)

- Passed / completed / open: green `#2e7d32` (background `#e8f5e9`)
- In progress / pending: amber `#b87333` (background `#fff3cd`)
- Failed / locked / blocked: muted red `#b71c1c` (background `#fee5e0`)

### Typography

- **Font family:** `"Segoe UI", "Arial Hebrew", "David", "Frank Ruehl", Arial, sans-serif` — applied to `<html>` and inherited everywhere
- **Body size:** 15px, line-height 1.65–1.70
- **Headers:** weight 700, color primary navy `#1a2638`. H1 28px, H2 22px, H3 17–18px, H4 15px
- **Code / formulas:** `"Courier New", "Consolas", monospace`, displayed in soft-bordered boxes for emphasis
- Numbers in calculations use thousands separators with commas; currency in shekels written as `1,200,000 ש"ח` (no symbol shorthand)

### Layout

- Max content width: 1080px, centered with `margin: 0 auto`
- Generous whitespace: 32–48px page padding, 24–32px between major sections
- Subtle box-shadow on content containers: `0 0 24px rgba(0,0,0,0.05)`
- Soft rounded corners: 3–4px radius (no harsh squares, no overly soft pills)
- RTL throughout: `<html dir="rtl" lang="he">` always, content right-aligned, borders and accents on the right side of cards

### Tone Rules — What to Avoid

- ❌ No hard contrasts (no pure black on pure white)
- ❌ No neon, no saturated primaries (no `#ff0000`, no `#00ff00`)
- ❌ No gradients except a single subtle navy gradient on the main phase banner
- ❌ No emojis in UI strings (we are a credit committee context, not a consumer app)
- ❌ No animation beyond hover state changes and progress bar fills
- ❌ No drop shadows on text
- ❌ No web fonts other than the system stack defined above

### Tailwind Approach

Tailwind via CDN, but with a small inlined config block in `base.html` that **extends the default palette** with semantic names matching the values above:

```html
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          cream: '#f5f5f0',
          navy: '#1a2638',
          slate: '#2c3e50',
          gold: '#f1c40f',
          muted: '#6b7280',
          'border-soft': '#cbd5e0',
        }
      }
    }
  }
</script>
```

Use semantic class names throughout templates (e.g., `bg-cream`, `text-navy`, `border-border-soft`). Do not hand-pick hex codes in templates.

### Print-Friendliness

Every page (except interactive ones like exam-taking) should print cleanly. Include `@media print` rules in the base stylesheet to:
- Hide navigation, footer, action buttons
- Use white background and black text where appropriate
- Avoid page breaks inside cards, callouts, and tables

The completed UI should look — when screenshot — like something appropriate to email to a credit committee chairman. If it doesn't, it's wrong.

---

## Data Model (Required Tables)

Build Django models that produce roughly this schema. Names in English (snake_case for fields). Add `created_at`, `updated_at`, soft-delete `is_active` on all relevant tables.

### Identity & Roles
- `User` — Django custom user. Fields: `email`, `username`, `full_name_he`, `full_name_en`, `role` (enum: `trainee`, `customer_manager`, `admin`, `ceo`), `supabase_user_id`, `is_active`.
- `Role` permissions handled via Django Groups + custom decorators.

### Content Hierarchy
- `Domain` — e.g., "Real Estate Finance — Israel". Fields: `name_he`, `name_en`, `description_he`, `slug`, `display_order`.
- `Course` — belongs to a `Domain`. Fields: `title_he`, `description_he`, `slug` (unique, used in URLs), `phase` (A/B/C/D/E), `course_number` (1–12), `passing_score_pct` (default 75), `exam_question_count`, `exam_duration_minutes`, `is_capstone` (bool).
- `Module` — belongs to `Course`. Fields: `title_he`, `slug` (unique within course), `module_number`, `estimated_minutes`.
- `ModuleComponent` — belongs to `Module`. Fields: `component_type` (enum: `reading`, `comprehension`, `exercises`, `summary`), `order`, `body_html_he` (for reading/summary), `instructions_he`.

### Questions
- `Question` — belongs to a `Module` (or to a `Course` for exam-level pool questions). Fields:
  - `question_id_external` (e.g., `C01-M04-Q07`)
  - `question_type` (1–6: retrieval, single-step calc, multi-step calc, document analysis, scenario, synthesis)
  - `difficulty` (`basic`, `intermediate`, `advanced`)
  - `stem_html_he` (rich HTML)
  - `image_url` (nullable, for document-analysis questions)
  - `points` (1–3)
  - `avg_time_seconds`
  - `usage_context` (enum: `comprehension`, `practice`, `exam`)
  - `topic_tags` (M2M to a `Tag` table)
  - `senior_insight_he` (short prose, written in the voice of a senior credit analyst, explaining the BUSINESS meaning of getting this question right or wrong — e.g., "An LTV miscalculation here would have killed the deal at credit committee." Shown to the trainee on the result screen alongside the technical explanation.)
  - `created_by`, `reviewed_by`, `last_calibrated_at`
  - `version` (integer, incremented on every edit — used to make snapshots traceable)
- `QuestionOption` — belongs to a `Question`. Fields: `text_he`, `is_correct` (bool), `display_order`, `distractor_rationale_he` (why this distractor exists; what error it represents).
- `QuestionExplanation` — one per question. Field: `explanation_html_he`.

### Enrollment & Progress
- `CourseEnrollment` — links `User` to `Course`. Fields: `status` (FSM-managed: `locked` → `requested` → `open` → `in_progress` → `passed`/`failed`, with re-open transitions), `unlocked_by` (FK User), `unlocked_at`, `completed_at`. **Use django-fsm decorators on transition methods** (e.g., `request_unlock()`, `approve_unlock()`, `start_course()`, `mark_passed()`). Direct status assignment forbidden.
- `UnlockRequest` — student requests course access. Fields: `user`, `course`, `status` (FSM: `pending` → `approved`/`denied`), `requested_at`, `responded_by`, `responded_at`, `note`.
- `ModuleProgress` — links `User` to `Module`. Fields: `started_at`, `completed_at`, `is_completed` (bool), `practice_score_pct`.
- `ComponentProgress` — links `User` to `ModuleComponent`. Fields: `is_completed`, `completed_at`. (Used for "I've finished reading" gates.)

### Exams
- `ExamAttempt` — belongs to `User` × `Course`. Fields: `attempt_number`, `status` (FSM: `in_progress` → `submitted` → `graded`), `started_at`, `submitted_at`, `score_pct`, `passed` (bool), `time_remaining_seconds_snapshot`, `is_locked` (after submit).
- `ExamAttemptQuestion` — links an attempt to a specific question, in display order. **Stores a complete snapshot of the question and its options as they existed when the attempt began.** Fields:
  - `display_order`
  - `question` (FK to live Question, for analytics — but never used for grading or display)
  - `question_version_at_attempt` (integer, the `Question.version` value at attempt start)
  - `stem_html_snapshot` (frozen copy of the stem text)
  - `options_snapshot_json` (frozen JSON array of `[{text, is_correct, distractor_rationale}, ...]` as they were)
  - `correct_option_index_snapshot`
  - `senior_insight_snapshot_he`
  - `explanation_snapshot_html_he`
  - `user_answer_option_index` (the index in the snapshot array)
  - `confidence_marked` (enum: `confident`, `not_sure`, `null` — trainee can optionally mark "I'm not sure" before answering; surfaces guessing patterns to managers in reports)
  - `answered_at`
  - `is_correct` (computed at submit time against `correct_option_index_snapshot`)

This snapshot mechanism is **non-negotiable**: if an admin edits a question while a trainee is mid-exam, the trainee continues to see and be graded against the snapshot, not the live question.

### Capstone (Course 12)
- `CapstoneSubmission` — belongs to `User`. Fields: `course` (FK to course 12), `file_url` (Supabase Storage URL to .docx), `submitted_at`, `status` (enum: `submitted`, `under_review`, `passed`, `failed`).
- `CapstoneRubricScore` — belongs to `CapstoneSubmission`. Fields: `category` (enum: 5 categories per spec), `score` (1–5), `comment_he`, `scored_by` (FK User).

### Documents
- `LearningDocument` — fields: `title_he`, `description_he`, `file_url` (Supabase Storage), `file_type` (enum: `pdf`, `docx`, `xlsx`, `image`), `domain` (FK), `tags` (M2M).
- `DocumentTag` — fields: `name_he`, `name_en`, `slug`.
- `DocumentAccessLog` — every download is logged. Fields: `user`, `document`, `accessed_at`.

### Audit & Reporting
- `AuditLog` — fields: `user`, `action` (enum), `entity_type`, `entity_id`, `metadata_json`, `created_at`. Every meaningful action writes here.
- `Notification` — stub table for future email. Fields: `user`, `type`, `payload_json`, `created_at`, `sent_at` (nullable). Don't actually send in MVP; just write the rows.

---

## Functional Requirements by Role

### All Users (after login)
- Personal dashboard showing: name, role, last login, list of courses with status (locked / requested / open / passed / failed).
- Profile page (read-only for trainees; editable name only).
- Logout.

### Trainee (20 users)
- See assigned domain (Real Estate Finance) and all 12 courses with status.
- For courses with status `locked`: button "Request Access". Submitting creates an `UnlockRequest` record.
- For courses with status `open`/`in_progress`: enter the course, see module list with progress, enter modules.
- Module screen: shows the four components (reading → comprehension → exercises → summary) sequentially. Forward gating: cannot access component N+1 until N is marked complete.
- Reading component: scroll-to-90% required before "I've finished reading" button activates.
- Comprehension check: 4 questions, immediate feedback, no scoring weight.
- Practice exercises: 6 questions, 2 attempts each, immediate feedback after answer (with distractor rationale shown), score recorded per module.
- Summary: read-only, marks module complete.
- Final exam: only available after all modules marked complete. Forward navigation only, timer visible, submit button with "are you sure" dialog. **Optional confidence marker** on each question — trainee can tag "I'm confident" or "I'm not sure" before submitting that question (default: unset). After submission: immediate score, breakdown by question type, list of incorrect answers with full **technical explanation + senior insight** (the "Committee Voice" line written in the tone of a senior credit analyst that explains the business consequence of the mistake — pulled from `senior_insight_snapshot_he`).
- Capstone (course 12 only): in addition to exam, file upload form for a .docx Word document.
- Search learning documents (open to all users).
- View own progress and exam history.

### Customer Manager (3 users)
- Everything a trainee sees, plus:
- "Trainees" section: list of all 20 trainees with summary stats (courses passed, in progress, locked, pending requests).
- Per-trainee detail: full progress, exam history, attempts, time spent.
- "Unlock Requests" inbox: list of pending `UnlockRequest` records. Approve / Deny actions, with optional note.
- "Capstone Reviews" inbox: pending `CapstoneSubmission` records. Click to download .docx, then fill rubric form (5 categories × 1–5 scale) inline. Submit triggers status transition.
- "Group Reports" page: aggregated stats on the cohort (avg completion %, avg exam score per course, time-to-pass distribution, struggling-trainee flag).
- **"Confidence Map" report** (per course or per module): shows which questions trainees most often answered correctly while marking "not sure" (true guesses that succeeded — content may be too easy to game), and which questions trainees most often answered incorrectly while marking "confident" (they thought they knew — the question or the underlying content needs review). This is a content-quality and pedagogy tool, not a punishment tool.

### Admin (1 user)
- Full Django Admin access — primary interface for content management.
- Manage `Domain`, `Course`, `Module`, `ModuleComponent`, `Question`, `QuestionOption`, `LearningDocument`, `DocumentTag`.
- Manage `User` records (create, deactivate, reset role).
- Bulk import questions via CSV/JSON (Django management command + admin action).
- View `AuditLog`.
- Cannot modify exam attempts or grades (those are immutable post-submit).

### CEO (1 user)
- Read-only access to everything.
- Same dashboards as Customer Manager, plus access to Audit Log read view.
- Export reports as CSV.

---

## Pedagogical / Exam Mechanics — Critical

- **Question rotation.** Course exam draws N questions from a pool of ≥3N available, randomly per attempt, weighted to maintain the type distribution (30% retrieval / 30% calc / 25% document / 15% scenario).
- **Forward-only navigation.** Once a question is answered, no return.
- **Auto-save.** If browser closes mid-exam, the timer continues server-side; user resumes at the same question on next login.
- **Time enforcement.** Server-side timer. On expiry, auto-submit whatever was answered.
- **Locked submissions.** Once submitted, an `ExamAttempt` is immutable.
- **Fully automatic grading.** All multiple-choice exams (every course 1–12) are graded automatically and instantly by the system on submit. There is **no manual review** of multiple-choice answers by anyone — not customer manager, not admin, not CEO. The trainee sees the score immediately on the result screen along with a per-question explanation. Customer managers' grading involvement is **strictly limited to the capstone .docx file** (course 12 only) — everything else is auto-graded.
- **Retry logic.**
  - Failed first attempt → 24-hour cooldown, then attempt 2 with ≥70% different question pool.
  - Failed second → 72-hour cooldown + mandatory mentor session (manual flag set by customer manager) before attempt 3.
  - Beyond third → admin override required.
- **Passing scores per spec doc:** default 75%, courses 5/8/9/11 are 80%, course 12 is 80% on exam + rubric thresholds.

---

## Project Files — Required Deliverables

Every one of these MUST be created and committed:

### `README.md`
Project overview and setup instructions. The setup section assumes the developer has already created and activated their own conda environment. Document the prerequisite and the install steps:

```bash
# Prerequisite: developer has created and activated their conda env, e.g.:
#   conda create -n <your-env-name> python=3.11 -y
#   conda activate <your-env-name>
# (env creation is done by the developer, not by Claude or any script)

# Inside the active conda env, install dependencies:
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Configure environment variables
cp .env.example .env   # then fill in the real values

# Database & first run
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Continue with: `.env` variable explanation, Supabase project setup (create project, copy URL and keys, set up storage bucket), how to seed initial data, deploy-to-Railway steps (connect GitHub repo, set env vars in Railway dashboard, deploy), how to run management commands (importing questions, importing documents).

### `CLAUDE.md`
Project conventions for future Claude Code sessions. Include:
- Project context (1 paragraph)
- **Conda env verification as the first step of every session** — confirm the conda env is already active before doing anything else; never attempt to create or switch envs
- Tech stack reference
- Directory structure with purpose of each folder
- Coding standards (PEP 8, type hints, docstring format)
- How models, views, templates are organized
- How to add a new course/module/question (data flow)
- Testing conventions (pytest, where tests live)
- Common commands
- Things NOT to do (e.g., "do not use raw SQL — use ORM", "do not bypass RBAC decorators", "do not install dependencies outside the conda env")

### `requirements.txt`
Pinned versions of all dependencies. Include at minimum: `Django>=5.0`, `psycopg2-binary`, `django-environ`, `supabase` (Python client), `gunicorn`, `whitenoise`, `Pillow`, `django-storages`, `django-fsm` (state machines for status transitions), `python-docx` (for Capstone auto-draft generator), `django-axes` (login rate limiting), `pytest-django`.

Also generate `requirements-dev.txt` for dev-only tools (pytest, black, ruff, factory-boy, ipython).

### `.gitignore`
Standard Python + Django + IDE ignores: `__pycache__`, `*.pyc`, `.env`, `venv/`, `.venv/`, `db.sqlite3`, `media/`, `staticfiles/`, `.idea/`, `.vscode/`, `.cursor/`, `*.log`, `.DS_Store`.

### `.env.example`
Template environment file documenting every required env var with placeholder values. NEVER commit a real `.env`. Variables to include:
- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG` (default False in production)
- `DJANGO_ALLOWED_HOSTS`
- `DATABASE_URL` (Supabase connection string)
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_KEY`
- `SUPABASE_STORAGE_BUCKET`
- `RAILWAY_STATIC_URL` (if needed)
- `EMAIL_BACKEND` (set to no-op for MVP)

### `Procfile` and `railway.json`
For Railway deployment. `Procfile` should run gunicorn; `railway.json` configures build/start commands.

### `runtime.txt`
Pin Python version (e.g., `python-3.11`).

---

## Build Phases — Iterative Plan

Build phase by phase. After each phase, summarize what's done and ask the user before proceeding to the next.

### Phase 1 — Project Bootstrapping

**Step 0 — Verify the conda environment is active (do this FIRST).**

The user has already created and activated a dedicated conda environment for this project. Your first action in any session is to **verify** the environment, not to create it.

Run these verification commands and confirm to the user:

```bash
# Verify Python comes from a conda env
python --version             # expect 3.11.x
which python                 # expect a conda env path (e.g., .../envs/<name>/bin/python)
echo $CONDA_DEFAULT_ENV      # should print the env name (not "base")
```

If any of these fail or show the wrong env, STOP and ask the user to activate the correct env before continuing.

Once verified, install Python dependencies via `pip` *into the active conda env*:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

After install: run `pip list` and confirm Django, psycopg2-binary, supabase, etc. all appear. Report the active env name and Python version back to the user.

**You must never:**
- Create a new conda env (the user owns env creation).
- Switch envs.
- Use `venv` or `virtualenv`.
- Install packages globally (outside the active env).
- Run `conda install` for project dependencies — use `pip` only, so `requirements.txt` remains the single source of truth.

**Step 1 — Repository and project skeleton.**
- Initialize git repo and connect to GitHub (instruct the user how to do this; do not push without explicit permission).
- Create Django project structure with apps: `core`, `accounts`, `content`, `enrollment`, `exams`, `capstone`, `documents`, `reports`.
- Set up `requirements.txt`, `requirements-dev.txt`, `.gitignore`, `.env.example`, `README.md`, `CLAUDE.md`, `Procfile`, `runtime.txt`, `railway.json`.
- Configure Django settings split: `base.py`, `dev.py`, `prod.py`.
- Set up Supabase connection via `DATABASE_URL`.
- Configure Tailwind CSS via CDN with the custom palette config from the Visual Design section.
- Set up RTL Hebrew base template with proper `<html dir="rtl" lang="he">`.
- **Configure Israeli timezone**: in settings, set `TIME_ZONE = 'Asia/Jerusalem'`, `USE_TZ = True`, `LANGUAGE_CODE = 'he'`. Document in CLAUDE.md that all cooldowns and timestamps are wall-clock Israel time.
- **Build a Hebrew/RTL middleware**: in `core/middleware/rtl.py`, create middleware that sets `Content-Language: he` on every response and injects `direction: 'rtl'` into the template context automatically. Wire it into `MIDDLEWARE` in settings.
- **Build the StorageService abstraction**: create `core/services/storage.py` with the interface described in Architectural Principle #9. The MVP implementation wraps Supabase Storage. Test with a stub upload of a placeholder file.

**Done when:**
- The (pre-existing) active conda env contains all dependencies from both requirements files; `pip list` confirms.
- Local dev server runs (`python manage.py runserver`).
- A stub home page renders in Hebrew RTL with the correct color palette.
- `python manage.py migrate` runs cleanly against Supabase.
- Git repo initialized; `.env` is in `.gitignore` and is NOT tracked.

### Phase 2 — Data Model
- Build all models per the data model section above.
- Migrations run cleanly.
- Populate seed data: one `Domain` ("Real Estate Finance — Israel"), 12 `Course` records (numbered 1–12 per the spec), and stubs for first module + first reading component of Course 1 Module 4 (use the sample module's content).
- Add Django Admin registrations for all models with sensible `list_display`, `search_fields`, `list_filter`.
- **Done when:** admin panel shows all entities, seed data visible, foreign-key relationships navigable.

### Phase 3 — Auth & Roles
- Custom user model with `role` field.
- Supabase Auth integration: login form posts to a Django view that authenticates against Supabase, then creates/updates a local `User` record with the Supabase user ID.
- Logout, session management, CSRF.
- Role-based decorators: `@trainee_required`, `@manager_required`, `@admin_required`, `@ceo_required` (and combinations).
- Stub dashboards per role with role-appropriate placeholder text.
- **Done when:** four test users (one per role) can log in and see their respective stub dashboards; unauthorized cross-role access returns 403.

### Phase 4 — Trainee Experience
- Trainee dashboard with course list (status badges).
- Course detail view: module list with status.
- Module view: 4-component flow (reading → comprehension → exercises → summary) with forward gating.
- "Request Access" button on locked courses → creates `UnlockRequest`.
- Practice exercise UI: question display, option select, immediate feedback after answer, distractor rationale.
- Final exam UI: timer, forward-only nav, auto-save, server-side time enforcement, submit dialog, immediate score with breakdown.
- **Done when:** a trainee user can be unlocked into Course 1 (manually via admin), navigate Module 4 (the seeded one), complete all four components, take the practice exercises, and take a final exam end-to-end with proper scoring.

### Phase 5 — Customer Manager Experience
- Trainees list page with summary stats.
- Per-trainee detail view.
- Unlock Requests inbox with approve/deny.
- Group Reports page (basic version: counts and averages).
- **Done when:** a customer manager can approve a request, view a trainee's progress, and see a basic group report.

### Phase 6 — Admin Experience
- Django Admin polished: useful list views, filters, search, inline editing for QuestionOptions.
- Bulk question import: management command `python manage.py import_questions <path>` accepting CSV or JSON.
- Bulk document import: `python manage.py import_documents <path>`.
- **Done when:** admin can add a new course + 5 modules + 30 questions via admin and CSV import in under 30 minutes.

### Phase 7 — Capstone (Course 12)
- File upload form for trainee (.docx only, ≤25 MB, validated server-side).
- Capstone Reviews inbox for customer managers.
- Rubric scoring form (5 categories × 1–5 scale + comment).
- Status transitions (FSM) and notifications-stub.
- **Capstone Auto-Draft Generator (stretch feature for MVP, ship if time permits).** A management command + admin button that takes the trainee's previous course exercises (financial calculations, document analyses, scenario answers) and produces a starter `.docx` template of a credit memorandum with sections pre-populated where data exists (e.g., the financial summary section pulls from their Course 9 modeling exercises; the risk section pulls from Course 10 scenario answers). The trainee then edits and refines this draft. Use `python-docx` to generate. If MVP time pressure forces a cut, defer this to v1.1 and document in CLAUDE.md.
- **Done when:** a trainee can submit a .docx file; a customer manager can review and score it; the trainee sees the result. Auto-draft generator is ideally working but optional for MVP sign-off.

### Phase 8 — Reports, Audit, Polish
- CEO reports view with CSV export.
- Audit log read view for CEO/Admin.
- Document search across `LearningDocument` table (basic full-text or trigram search).
- Capstone-deliverable archive view.
- Email notification stub class wired up to write `Notification` rows on key events.
- Production deployment to Railway, env vars set, smoke-tested live.
- **Done when:** the system is deployed, all roles can perform their workflows on the live URL, no critical bugs.

---

## Coding Standards

- **Python.** PEP 8. Black formatting (line length 100). Ruff for linting. Type hints on all function signatures.
- **Django.** Class-based views where it simplifies; function views where they don't. Use `select_related` / `prefetch_related` to avoid N+1.
- **Templates.** Single `base.html` with RTL setup. Component-style includes. Tailwind classes inline.
- **Naming.** Models in English, model field names in English snake_case. UI strings in Hebrew via `gettext_lazy` (set up i18n from day one even if Hebrew is the only language for now — this preserves the option to add languages).
- **Tests.** pytest-django. Aim for coverage on models, views, permissions, and exam-grading logic. Don't waste time on trivial tests.
- **Commits.** Conventional commits (`feat:`, `fix:`, `chore:`, `refactor:`, `test:`, `docs:`). Small, focused commits.
- **Branches.** Work on `main` for solo MVP development, but tag major phase completions (e.g., `v0.1-phase1-bootstrap`).

---

## Security Baseline

- HTTPS enforced in production (Railway provides this; configure `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`).
- CSRF protection on all forms.
- Password hashing via Supabase Auth (never store plaintext).
- Server-side validation of every form (never trust client).
- File upload validation: type, size, content-type sniffing.
- SQL injection: Django ORM only, no raw SQL unless absolutely necessary and parameterized.
- XSS: Django auto-escaping on; carefully review any `|safe` usage in templates.
- Rate limit login attempts (django-axes or similar).
- Logging: log auth events, exam submissions, capstone uploads, role changes. Never log passwords or PII bodies.

---

## Email — Stub for Future

Build an `EmailService` class in `core/services/email.py` with methods for events you'll likely need:
- `send_welcome(user)`
- `send_unlock_approved(user, course)`
- `send_unlock_denied(user, course, reason)`
- `send_exam_passed(user, course, score)`
- `send_exam_failed(user, course, score, attempts_remaining)`
- `send_capstone_received(user)`
- `send_capstone_graded(user, passed)`
- `send_manager_unlock_request(manager, request)`

In MVP, each method writes a `Notification` row and logs `[EMAIL_STUB] would send X to Y`. Backend selection in `settings.EMAIL_BACKEND` controls behavior; future swap to a real provider is a config change only.

---

## What NOT to Build in MVP

To stay focused, explicitly skip:
- Mobile responsive design.
- Multi-language UI (Hebrew only).
- Real-time features (websockets, live notifications).
- Sophisticated analytics dashboards (basic counts and tables only).
- Question bank calibration analytics (capture data only — no UI).
- Plagiarism detection on capstone uploads.
- Single sign-on / OAuth providers.
- Payment / billing.
- Public marketing pages.

Document these in `CLAUDE.md` under "Out of Scope for MVP" so future contributors understand intentional omissions.

---

## Definition of Done — Overall MVP

The MVP is complete when:
1. A new trainee can be created by admin, log in, request access to a course, be approved by a manager, complete all modules of a course, take and pass the final exam, and see their result history.
2. A capstone trainee can upload a .docx, a manager can grade it, and the trainee sees pass/fail.
3. A CEO can view a group report and export to CSV.
4. The admin can add a new course, modules, and questions entirely through Django Admin or management commands without touching code.
5. The system is deployed to Railway and reachable at a live URL with HTTPS.
6. `README.md`, `CLAUDE.md`, `.env.example`, `requirements.txt`, `.gitignore`, `Procfile`, `railway.json`, `runtime.txt` all exist and are accurate.
7. Adding a second domain ("Commercial Banking") would require zero schema changes — only data inserts.

---

## Working Style Instructions

- After each build phase, write a short summary of what was done and ask the user to confirm before moving on.
- When you make a non-trivial design decision (e.g., "I'm using `django-storages` for Supabase Storage integration"), state it explicitly.
- Don't refactor code from earlier phases without asking — phase outputs are stable contracts.
- If a requirement is ambiguous, ask. Do not infer silently.
- Prefer simple solutions. Reach for libraries only when meaningfully shorter than the manual approach.
- Test in Hebrew RTL from day one — do not let LTR sneak in then "fix later".
- Keep `CLAUDE.md` updated as you go — it's the handoff document for the next session.

---

## Reference Quick Links (within project)

- Curriculum spec: `./curriculum_specification_v2.html`
- Sample module: `./sample_module_C01M04.html`
- This prompt: `./BUILD_PROMPT.md`

When in doubt about WHAT to build, the spec doc and sample module are authoritative. When in doubt about HOW to build, this document is authoritative.

Begin with Phase 1.
