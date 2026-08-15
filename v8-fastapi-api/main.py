"""
Enterprise RAG System

Version 8 - FastAPI REST API

Author
------
Shiva Shankar Reddy

Description
-----------
Main FastAPI application.
Creates the API instance and registers all routes.
"""

from fastapi import FastAPI

from api.routes import router
from services.chroma_service import ChromaService
from services.indexing_pipeline import IndexingPipeline

# ============================================================
# Initialize Vector Database
# ============================================================

db = ChromaService()

print("=" * 40)
print("Total vectors in ChromaDB:", db.count())
print("=" * 40)

if db.count() == 0:
    print("\nNo vectors found. Running indexing pipeline...\n")
    IndexingPipeline().run()
else:
    print("\nVector database already initialized.\n")

# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title="Enterprise RAG System API",
    description="REST API for the Enterprise RAG System",
    version="8.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ============================================================
# Register Routes
# ============================================================

app.include_router(router)

# ============================================================
# Root Endpoint
# ============================================================

@app.get("/", tags=["Root"])
def root():
    """
    Root endpoint.
    """
    return {
        "message": "Welcome to Enterprise RAG System API",
        "version": "8.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health",
    }

# ============================================================
# Run Application
# ============================================================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )