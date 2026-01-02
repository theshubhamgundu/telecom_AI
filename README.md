# TelecomCare AI: Advanced Support Agent

TelecomCare AI is a high-performance, personalized support assistant designed for the telecom industry. It provides a seamless mobile dashboard experience (Airtel/Vi style) integrated with a history-aware AI chat and automated voice call escalation.

## 🚀 Key Features

- **Personalized Dashboard**: View real-time data balance, plan validity, and account status with a premium Airtel-inspired UI.
- **History-Aware Chat**: The AI remembers your previous interactions (e.g., recurring network issues) and adjusts its support accordingly.
- **AI Voice Call Escalation**: Automatically initiates an AI voice agent call if technical issues persist or if the user requests human-like voice support.
- **Smart Suggestions**: Quick-reply chips for common actions like checking balance or reporting network issues.
- **RAG-Ready Architecture**: Built on FastAPI, ready for integration with Large Language Models (LLMs) and Vector Databases (ChromaDB).

## 🛠️ Project Structure

```text
├── api/                  # Vercel serverless entry points
├── static/               # Premium Frontend (HTML/CSS/JS)
│   └── index.html        # Main Airtel-style App UI
├── main.py               # FastAPI Backend Logic
├── userdata.json         # Mock User Database (History/Context)
├── tickets.json          # Support Ticket Management
├── requirements.txt      # Python Dependencies
└── vercel.json           # Cloud Deployment Configuration
```

## 💻 Tech Stack

- **Frontend**: Vanilla HTML5, CSS3 (Custom Design System), JavaScript (ES6+), Lucide Icons.
- **Backend**: Python, FastAPI.
- **Data**: JSON-based mock storage (Scalable to PostgreSQL/MongoDB).

## 🚦 Getting Started

### 1. Installation
Ensure you have Python 3.8+ installed.
```bash
pip install -r requirements.txt
```

### 2. Run Locally
```bash
python main.py
```
Visit **http://localhost:8000** to explore the dashboard.

### 3. Core Endpoints
- `GET /`: Serves the mobile dashboard.
- `POST /chat`: AI chat interface (Supports history & escalation).
- `GET /health`: System health status.

## 🤖 How the AI Works

The agent uses a decision-engine that:
1. **Identifies Context**: Loads user data and history from `userdata.json`.
2. **Personalizes Response**: Greets users by name and references their specific plan and past issues.
3. **Escalates when Needed**: If a user reports "slow internet" twice, or explicitly asks to "talk", the backend triggers a `needs_escalation` flag, which the frontend handles by showing a "Calling AI Agent" UI.

---
*Developed for Group AC - Telecom AI Innovation.*
