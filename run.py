from serverless_wsgi import handle_request  # Make sure you have this package in your requirements
from flask import Flask, jsonify
from app.api.endpoints.background_removal import background_removal
from app.api.endpoints.human_segmentation import human_segment
from app.api.endpoints.segment_and_remove_background import segment_and_remove_background_bp as segment_and_remove_bg
import logging
logging.basicConfig(level=logging.DEBUG)

def create_app():
    """
    Create and configure the Flask application.

    This function sets up the application, registers blueprints, 
    and sets up error handlers for a consistent API response.

    Returns:
        app: A Flask application instance.
    """

    app = Flask(__name__)

    # Register blueprints with versioning
    register_blueprints(app)

    # Set up error handlers for consistent API response
    register_error_handlers(app)

    return app

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

app = create_app()


if __name__ == '__main__':
    app.run(port=5002)
