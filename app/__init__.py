from flask import Flask, jsonify
from app.api.endpoints.background_removal import background_removal
from app.api.endpoints.human_segmentation import human_segment
from app.api.endpoints.segment_and_remove_background import segment_and_remove_background_bp as segment_and_remove_bg
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def register_blueprints(app):
    """
    Register the application blueprints.

    This function registers the application blueprints and provides 
    versioning to the API endpoints.

    Args:
        app (Flask): The Flask application instance.
    """

    api_version = "/v1"  # for example
    app.register_blueprint(background_removal, url_prefix=f'/api{api_version}')
    app.register_blueprint(human_segment, url_prefix=f'/api{api_version}')
    app.register_blueprint(segment_and_remove_bg, url_prefix=f'/api{api_version}')

def register_error_handlers(app):
    """
    Register error handlers for the application.

    This function sets up error handlers for consistent API response in 
    case of errors.

    Args:
        app (Flask): The Flask application instance.
    """

    @app.errorhandler(404)
    def not_found(e):
        """
        Handle 404 errors.
        
        Args:
            e (Exception): The raised exception.

        Returns:
            Response: A JSON response with the error message.
        """
        return jsonify(error=str(e)), 404

    @app.errorhandler(500)
    def internal_error(e):
        """
        Handle 500 errors.
        
        Args:
            e (Exception): The raised exception.

        Returns:
            Response: A JSON response with the error message.
        """
        return jsonify(error=str(e)), 500



