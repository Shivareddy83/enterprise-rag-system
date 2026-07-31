"""
Enterprise RAG System
Version 9

Application Entry Point
"""

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.routes import router

# ======================================================
# Logging
# ======================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("enterprise_rag")

# ======================================================
# Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent

FRONTEND_DIR = BASE_DIR / "frontend"
STATIC_DIR = FRONTEND_DIR / "static"
TEMPLATE_DIR = FRONTEND_DIR / "templates"

# ======================================================
# Lifespan
# ======================================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("=" * 60)
    logger.info("Enterprise RAG System Starting...")
    logger.info("Version 9.0")
    logger.info("=" * 60)

    yield

    logger.info("Enterprise RAG System Stopped.")

# ======================================================
# FastAPI
# ======================================================

app = FastAPI(
    title="Enterprise RAG System",
    version="9.0",
    description="Enterprise Retrieval-Augmented Generation System",
    lifespan=lifespan,
)

# ======================================================
# Static Files
# ======================================================

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)

templates = Jinja2Templates(
    directory=str(TEMPLATE_DIR)
)

# ======================================================
# API
# ======================================================

app.include_router(
    router,
    prefix="/api/v1",
    tags=["API"],
)

# ======================================================
# Frontend
# ======================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
        },
    )