from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import json

# Load environment variables
load_dotenv()

app = FastAPI(title="TelecomCare AI Support Agent")

# Helper to get absolute path
def get_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

# helper to load data
def load_json_data(filename, default):
    try:
        path = get_path(filename)
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
    return default

# Mock data as fallback if files are missing on Vercel
DEFAULT_USERS = {
    "9876543210": {
        "name": "Shubham Gundu",
        "plan": "Unlimited 5G",
        "data_limit": "1.5 GB/day",
        "data_used": "1.4 GB",
        "validity": "24 Days",
        "last_bill": "Rs. 299",
        "status": "Active",
        "history": [
            {"date": "2025-12-28", "query": "Slow internet", "resolution": "Network reset from backend"},
            {"date": "2025-12-30", "query": "Data balance check", "resolution": "Provided via SMS"}
        ]
    }
}

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static file paths for Vercel
static_dir = get_path("static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def root():
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Airtel Care AI (Static UI missing)", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "TelecomCare AI"}

@app.post("/chat")
async def chat_endpoint(request: dict):
    query = request.get("query", "").lower()
    phone_number = request.get("phone_number", "9876543210")
    
    users = load_json_data('userdata.json', DEFAULT_USERS)
    # tickets = load_json_data('tickets.json', []) # Not used in current logic but kept for extension
    
    user = users.get(phone_number, DEFAULT_USERS["9876543210"])
    user_name = user.get("name", "User")
    history = user.get("history", [])
    
    response_text = ""
    needs_escalation = False
    escalation_reason = ""

    # History-aware logic
    if "how it works" in query or "how do you work" in query or "features" in query:
        response_text = ("I am a 24/7 AI-powered support agent designed specifically for telecom needs. "
                         "I analyze your account status, usage patterns, and support history to provide personalized help. "
                         "If I detect recurring technical issues, I can automatically initiate an AI Voice Agent call to "
                         "your registered number for advanced diagnostics.")
    elif "balance" in query or "data" in query:
        response_text = f"Hi {user_name}, you have {user.get('data_used')} used out of {user.get('data_limit')}. Your plan is valid for {user.get('validity')}."
    elif "history" in query or "previous" in query:
        last_query = history[-1]['query'] if history else "No previous queries"
        response_text = f"Looking at your history, your last request was about '{last_query}'. Is there anything else related to that?"
    elif "slow" in query or "internet" in query or "network" in query:
        response_text = f"I see you've had network issues before (Resolved on 2025-12-28). Since this is recurring, would you like me to initiate an AI voice agent call to run a remote diagnostic?"
        if "yes" in query or "call" in query or "agent" in query:
            needs_escalation = True
            escalation_reason = "Recurring network issue"
            response_text = "Understood. I am initiating an AI Voice Agent call to your registered number right now for real-time troubleshooting."
    elif "call" in query or "talk" in query or "human" in query:
        needs_escalation = True
        escalation_reason = "User requested voice support"
        response_text = "Sure! I'm connecting you to our AI Voice Assistant for a personalized call."
    else:
        response_text = f"Hello {user_name}, I'm here to help. You can ask about your balance, history, or reported issues. You can also ask 'How does this work?' to learn more."

    return {
        "answer": response_text,
        "needs_escalation": needs_escalation,
        "escalation_type": "voice_call" if needs_escalation else None,
        "user_context": {
            "name": user_name,
            "plan": user.get("plan")
        }
    }

# For Vercel serverless deployment
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
