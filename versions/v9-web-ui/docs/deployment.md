# Deployment Guide

# Enterprise Knowledge Platform (EKP)

## Current Release

**Version 9 – Enterprise Web UI**

---

# Introduction

This guide explains how to deploy the Enterprise Knowledge Platform (EKP) in different environments.

Version 9 is designed primarily for local development, but its architecture supports deployment to production environments with minimal modifications.

This guide covers:

- Local Deployment
- Docker Deployment
- Docker Compose
- Reverse Proxy (Nginx)
- HTTPS
- Cloud Deployment
- Environment Variables
- Monitoring
- Maintenance

---

# Deployment Architecture

```
                    Internet
                        │
                        ▼
                 Nginx Reverse Proxy
                        │
                        ▼
                  FastAPI Application
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
     Google Gemini                 ChromaDB
```

---

# Prerequisites

Before deployment, ensure the following are installed.

## Required Software

- Python 3.11+
- Git
- pip
- Virtual Environment
- Google Gemini API Key

Optional:

- Docker
- Docker Compose
- Nginx

---

# Environment Configuration

Create a `.env` file in the project root.

Example:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Never commit the `.env` file to version control.

---

# Local Development Deployment

## Step 1

Clone the repository.

```bash
git clone https://github.com/your-username/enterprise-knowledge-platform.git
```

---

## Step 2

Navigate into the project.

```bash
cd enterprise-knowledge-platform
```

---

## Step 3

Create a virtual environment.

```bash
python -m venv venv
```

---

## Step 4

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

## Step 5

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Step 6

Start the application.

```bash
uvicorn backend.main:app --reload
```

---

## Step 7

Open your browser.

```
http://127.0.0.1:8000
```

The Enterprise Web UI should be available.

---

# Production Deployment

For production, avoid using the development server.

Recommended command:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

Recommended production server:

- Gunicorn (Linux/macOS)
- Uvicorn Workers
- Process Manager (systemd or Supervisor)

---

# Docker Deployment

Create a Docker image.

Example Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Build Image

```bash
docker build -t ekp:v9 .
```

---

## Run Container

```bash
docker run -p 8000:8000 --env-file .env ekp:v9
```

---

# Docker Compose

Example:

```yaml
version: "3.9"

services:

  ekp:

    build: .

    ports:
      - "8000:8000"

    env_file:
      - .env
```

Start services:

```bash
docker compose up --build
```

---

# Reverse Proxy (Nginx)

Example configuration:

```nginx
server {

    listen 80;

    server_name example.com;

    location / {

        proxy_pass http://127.0.0.1:8000;

        proxy_set_header Host $host;

        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

}
```

---

# HTTPS

For production deployments:

- Use HTTPS
- Install SSL certificates
- Redirect HTTP to HTTPS
- Renew certificates regularly

Let's Encrypt is a common choice for free SSL certificates.

---

# Cloud Deployment

The platform can be deployed to cloud providers such as:

- AWS
- Microsoft Azure
- Google Cloud Platform
- Render
- Railway

Deployment steps are similar:

1. Upload project.
2. Configure environment variables.
3. Install dependencies.
4. Start FastAPI.
5. Configure domain.
6. Enable HTTPS.

---

# Environment Variables

Example:

```env
GOOGLE_API_KEY=xxxxxxxxxxxxxxxx
```

Future variables may include:

```env
DATABASE_URL=
JWT_SECRET=
APP_ENV=
LOG_LEVEL=
```

---

# Health Check

Verify backend availability.

```
GET /health
```

Expected response:

```json
{
    "status": "ok"
}
```

---

# Monitoring

Monitor:

- API uptime
- Response time
- CPU usage
- Memory usage
- Disk usage
- Error logs

Recommended tools:

- Prometheus
- Grafana
- Uptime monitoring services

---

# Logging

Recommended logging includes:

- Startup events
- API requests
- Errors
- Warnings
- Exceptions

Store logs separately from application code.

---

# Backup Strategy

Recommended backups:

- Source code (Git)
- Configuration
- Environment templates
- Vector database (if persistent)
- Future relational databases

---

# Security Checklist

Before deploying to production:

- Keep API keys in environment variables.
- Disable debug mode.
- Enable HTTPS.
- Validate all user input.
- Restrict server access.
- Keep dependencies updated.

---

# Troubleshooting

## Application Will Not Start

Possible causes:

- Missing dependencies
- Incorrect Python version
- Missing environment variables

Solution:

```bash
pip install -r requirements.txt
```

---

## Invalid API Key

Verify:

```env
GOOGLE_API_KEY=your_actual_key
```

Restart the application after updating the `.env` file.

---

## Port Already in Use

If port `8000` is occupied, choose another port:

```bash
uvicorn backend.main:app --port 8080
```

---

## Docker Build Fails

Check:

- Docker installation
- Docker daemon status
- Dockerfile syntax

Rebuild:

```bash
docker compose build --no-cache
```

---

# Deployment Checklist

Before deployment, verify:

- Python installed
- Dependencies installed
- Environment variables configured
- API key configured
- Application starts successfully
- `/health` endpoint responds correctly
- Frontend loads successfully
- AI responses are generated correctly

---

# Current Scope (Version 9)

Supported deployment methods:

- Local Development
- Docker
- Docker Compose

Future releases will expand support for:

- Kubernetes
- CI/CD Pipelines
- Multi-container deployments
- Auto-scaling
- High Availability

---

# Summary

The Enterprise Knowledge Platform can be deployed locally for development or packaged for production using Docker and a reverse proxy such as Nginx.

Version 9 establishes a deployment foundation that supports future enterprise features, including cloud hosting, secure HTTPS communication, monitoring, automated deployments, and scalable infrastructure.