# Vercel Deployment Guide

## Quick Setup

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```

## Environment Variables

Set these in your Vercel dashboard:
- `GEMINI_API_KEY`: Your Google Gemini API key
- `TWILIO_ACCOUNT_SID`: Your Twilio account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio auth token

## Project Structure

```
├── api/
│   └── index.py          # Vercel serverless function entry point
├── main.py               # FastAPI application
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
├── package.json         # Node.js configuration
└── .vercelignore        # Files to ignore during deployment
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /chat` - Chat endpoint

## Notes

- Large data files (tickets.json, userdata.json) are excluded from deployment
- ChromaDB setup would need to be handled differently for serverless environment
- Current setup provides basic API functionality for demonstration
