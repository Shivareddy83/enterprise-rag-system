# User Guide

# Enterprise Knowledge Platform (EKP)

## Current Release

**Version 9 – Enterprise Web UI**

---

# Introduction

Welcome to the Enterprise Knowledge Platform (EKP).

This guide explains how to install, configure, launch, and use the platform effectively. Whether you are a developer, student, researcher, or enterprise user, this guide will help you get started with the AI-powered knowledge platform.

---

# System Requirements

Before installing EKP, ensure your system meets the following requirements.

| Component | Requirement |
|-----------|-------------|
| Operating System | Windows 10/11, Linux, macOS |
| Python | 3.11 or later |
| RAM | Minimum 8 GB (16 GB Recommended) |
| Storage | 2 GB Free Space |
| Internet | Required for Google Gemini API |

---

# Prerequisites

Install the following software before running the application:

- Python 3.11+
- Git
- Visual Studio Code (Recommended)
- Google Gemini API Key

---

# Installation

## Step 1 – Clone the Repository

```bash
git clone https://github.com/your-username/enterprise-knowledge-platform.git
```

Navigate to the project directory:

```bash
cd enterprise-knowledge-platform
```

---

## Step 2 – Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Linux/macOS:

```bash
python3 -m venv venv
```

---

## Step 3 – Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

---

## Step 4 – Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 – Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Replace `your_google_gemini_api_key` with your actual API key.

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

If the server starts successfully, you should see output similar to:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Accessing the Application

Open your web browser and visit:

```
http://127.0.0.1:8000
```

The Enterprise Web UI should load.

---

# Using the Platform

## Step 1 – Open the Web Interface

Launch the application in your browser.

You will see:

- Welcome screen
- Chat interface
- Sidebar
- Input box
- Server status indicator

---

## Step 2 – Ask a Question

Enter a question in the chat input.

Example:

```
Explain Retrieval-Augmented Generation.
```

Click the **Send** button or press **Enter**.

---

## Step 3 – AI Processing

The backend will:

1. Validate your question
2. Search the vector database
3. Retrieve relevant document chunks
4. Build a prompt
5. Send the prompt to Google Gemini
6. Generate a response

---

## Step 4 – View the Response

The AI response is displayed in the chat window.

Supported content includes:

- Paragraphs
- Lists
- Tables
- Code blocks
- Markdown formatting

---

# Exporting Conversations

Version 9 supports exporting conversations.

Available formats:

- TXT
- JSON
- PDF

To export:

1. Open the conversation.
2. Click the **Export** button.
3. Select the desired format.
4. Save the file.

---

# Checking Server Status

The status indicator shows the current backend state.

| Status | Meaning |
|--------|---------|
| 🟢 Online | Server is running |
| 🟡 Connecting | Attempting to connect |
| 🔴 Offline | Server unavailable |

---

# API Documentation

Interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

Alternative documentation:

```
http://127.0.0.1:8000/redoc
```

---

# Common Issues

## Application Does Not Start

Possible causes:

- Python not installed
- Missing dependencies
- Incorrect virtual environment

Solution:

```bash
pip install -r requirements.txt
```

---

## Invalid API Key

Symptoms:

- AI responses fail
- Authentication errors

Solution:

Verify the `.env` file:

```env
GOOGLE_API_KEY=your_actual_api_key
```

Restart the application after updating the key.

---

## Backend Offline

Symptoms:

- Health indicator shows **Offline**
- Requests fail

Solution:

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

---

## Dependencies Missing

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# Best Practices

For the best experience:

- Keep your dependencies up to date.
- Use clear and specific questions.
- Ensure the backend is running before opening the UI.
- Store API keys securely in environment variables.
- Regularly back up project files and configuration.

---

# Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Enter | Send Message |
| Shift + Enter | New Line |
| Ctrl + C | Stop Server (Terminal) |
| Ctrl + R | Refresh Browser |

---

# Updating the Project

To get the latest changes:

```bash
git pull origin main
```

If dependencies have changed:

```bash
pip install -r requirements.txt
```

---

# Uninstalling

To remove the project:

1. Delete the project directory.
2. Remove the virtual environment.
3. Delete any local configuration files (such as `.env`) if no longer needed.

---

# Frequently Asked Questions (FAQ)

### Does EKP require an internet connection?

Yes. Version 9 uses Google Gemini for AI response generation.

---

### Can I upload documents from the web interface?

Not in Version 9. This feature is planned for a future release.

---

### Can I use multiple users?

Version 9 is designed for a single-user development environment. Multi-user support is planned.

---

### Is authentication available?

No. Authentication is planned for future versions.

---

### Can I customize the UI?

Yes. The frontend can be modified by editing the HTML, CSS, and JavaScript files.

---

# Summary

The Enterprise Knowledge Platform provides a straightforward workflow:

1. Install the application.
2. Configure the environment.
3. Start the FastAPI server.
4. Open the Enterprise Web UI.
5. Ask questions about your knowledge base.
6. Review AI-generated responses.
7. Export conversations when needed.

Following this guide will help you set up and use Version 9 efficiently while preparing for future platform enhancements.