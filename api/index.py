def handler(event, context):
    """
    Minimal Vercel serverless function for debugging
    """
    try:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': '{"message": "TelecomCare AI is working!"}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': f'{{"error": "{str(e)}"}}'
        }

# Vercel entry point
def lambda_handler(event, context):
    return handler(event, context)
