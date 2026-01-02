def handler(request):
    """
    Main Vercel serverless function
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': '{"message": "TelecomCare AI is working!", "status": "healthy"}'
    }
