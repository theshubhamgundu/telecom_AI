from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="TelecomCare AI Support Agent")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "TelecomCare AI Support Agent API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "TelecomCare AI"}

@app.post("/chat")
async def chat_endpoint(request: dict):
    """
    Simple chat endpoint for Vercel deployment
    Note: Full RAG functionality would require ChromaDB setup
    """
    query = request.get("query", "")
    phone_number = request.get("phone_number", "")
    
    # Simple response for demo - replace with actual RAG logic
    response = {
        "answer": f"This is a demo response for: {query}",
        "sources": ["demo_source_1"],
        "needs_escalation": False
    }
    
    return response

# For Vercel serverless deployment
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
