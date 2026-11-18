# SupportPilot – Module 1: Ticket Processing & Classification

Employees sign up, raise tickets and see their ID and expected resolution time. The AI classifies each ticket
(category, sub-category, severity, priority). The admin sees every ticket with its classification and can close or reopen it.
Everything is password protected and stored in MySQL.

## Admin login (seeded on first run)
- Admin ID: `ADMIN001`
- Password: `SupportPilot@2026`  (change it in `config.py` BEFORE the first run; it is stored hashed)

## Setup (VS Code, Windows PowerShell)
1. Install MySQL 8 and make sure the server is running.
2. Open `config.py` and set `DB_PASSWORD` to your MySQL password (database `supportpilot` and its tables are created automatically).
3. Run:
```
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
4. Open http://127.0.0.1:5000 (the first run also trains the model).

## Structure
- `app.py` routes, login, sessions, ticket API | `db.py` MySQL tables | `ml.py` classifier + priority/SLA rules
- `src/make_dataset.py`, `src/train.py` training data and model | `templates/`, `static/` UI

## Rules implemented
- Employee: sign up (name, email, department, strong password), sees only their own tickets, no classification details.
- Admin: sees all tickets and classification results; closes/reopens tickets. Admin cannot sign up through the UI.
- Priority to resolve-within: P1 24 hrs, P2 48 hrs, P3 1 week, P4 4 weeks.
- Passwords are hashed, sessions expire after 8 hours, 5 failed logins lock that ID for 5 minutes, every page and API checks the role.

## Git steps (this part)
```
git add .
git commit -m "Module 1: login, MySQL storage, employee and admin dashboards"
git push
```
