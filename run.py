from app import create_app
import logging
from serverless_wsgi import handle_request  # Make sure you have this package in your requirements

logging.basicConfig(level=logging.DEBUG)

app = create_app()

def lambda_handler(event, context):
    """
    Handles the lambda event and context and returns the result.

    Args:
        event (dict): The event data passed to the lambda function.
        context (dict): The context object passed to the lambda function.

    Returns:
        The result of calling the handle_request function with the app, event, and context parameters.
    """  
    logger.debug("Starting lambda...")
    return handle_request(app, event, context)

if __name__ == '__main__':
    app.run(port=5002)
