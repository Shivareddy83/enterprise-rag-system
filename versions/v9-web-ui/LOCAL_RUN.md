# EKP V9 — Local Run & Verification

## 1. Configure

Copy `.env.example` to `.env` and add your Gemini key if you want `/api/v1/ask` to generate answers.

The backend can start without a Gemini key. `/api/v1/health` remains a liveness check; `/api/v1/health/dependencies` reports Gemini as unavailable.

## 2. Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Test

```powershell
python -m compileall -q .
python -m pytest -q
```

## 4. Run locally

```powershell
uvicorn main:app --reload --port 8000
```

Open `http://127.0.0.1:8000/`.

API docs: `http://127.0.0.1:8000/docs`

Liveness: `http://127.0.0.1:8000/api/v1/health`

Dependency health: `http://127.0.0.1:8000/api/v1/health/dependencies`

Vector count: `http://127.0.0.1:8000/api/v1/debug/count`

## 5. Functional flow

1. Open the UI and confirm `Online`.
2. Upload a PDF.
3. Confirm the upload reports indexed chunks/vectors.
4. Ask a question about the uploaded document.
5. Check the browser Network tab for `/api/v1/health`, `/api/v1/upload`, and `/api/v1/ask`.

## 6. Docker

```powershell
docker compose build
docker compose up -d
docker compose ps
docker compose logs -f ekp
```

The container exposes port `8000`.
