import json
from main import app
from mangum import Mangum

# Create a handler for Vercel serverless functions
handler = Mangum(app)

# Vercel entry point
def lambda_handler(event, context):
    return handler(event, context)
