import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# Create FastAPI app directly in serverless function
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

# Create a handler for Vercel serverless functions
handler = Mangum(app)

# Vercel entry point
def lambda_handler(event, context):
    return handler(event, context)
