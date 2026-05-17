# react-django-todo

Simple todo CRUD app: **Next.js** frontend + **Django REST Framework** backend with **SQLite**.

## Structure

```
react-django-todo/
├── backend/     Django API (port 8000)
└── frontend/    Next.js UI (port 3000)
```

## Setup

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

API: http://localhost:8000/api/todos/

### Frontend

```bash
cd frontend
npm install
npm run dev
```

App: http://localhost:3000

Copy `.env.local` is already set to `NEXT_PUBLIC_API_URL=http://localhost:8000/api`.

## API

| Method | URL | Action |
|--------|-----|--------|
| GET | `/api/todos/` | List todos |
| POST | `/api/todos/` | Create `{ "title": "..." }` |
| PATCH | `/api/todos/{id}/` | Update `{ "completed": true }` |
| DELETE | `/api/todos/{id}/` | Delete |

SQLite database file: `backend/db.sqlite3` (created on first `migrate`).
