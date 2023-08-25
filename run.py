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

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
