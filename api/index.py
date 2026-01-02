import json

def handler(request):
    """
    Simple Vercel serverless function handler
    """
    try:
        # Handle different request methods
        method = request.get('method', 'GET')
        path = request.get('path', '/')
        
        # CORS headers
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Content-Type': 'application/json'
        }
        
        # Handle OPTIONS preflight
        if method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': ''
            }
        
        # Route handling
        if path == '/' or path == '':
            response = {"message": "TelecomCare AI Support Agent API"}
        elif path == '/health':
            response = {"status": "healthy", "service": "TelecomCare AI"}
        elif path == '/chat' and method == 'POST':
            # Parse request body
            body = request.get('body', '{}')
            if isinstance(body, str):
                body = json.loads(body)
            
            query = body.get('query', '')
            phone_number = body.get('phone_number', '')
            
            response = {
                "answer": f"This is a demo response for: {query}",
                "sources": ["demo_source_1"],
                "needs_escalation": False
            }
        else:
            response = {"error": "Not found"}
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps(response)
            }
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({"error": str(e)})
        }

# Vercel entry point
def lambda_handler(event, context):
    return handler(event)
