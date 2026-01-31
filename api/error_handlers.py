"""
Error Handlers for E-Commerce Recommendation System
Centralized error handling for consistent API responses
"""

from flask import jsonify
from werkzeug.exceptions import HTTPException
from validators.validators import ValidationError
from config.constants import (
    HTTP_BAD_REQUEST, HTTP_NOT_FOUND, HTTP_INTERNAL_ERROR
)
import logging

logger = logging.getLogger(__name__)


def register_error_handlers(app):
    """
    Register all error handlers with the Flask app
    
    Args:
        app: Flask application instance
    """
    
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        """Handle validation errors"""
        logger.warning(f"Validation error: {str(error)}")
        return jsonify({
            'error': 'Validation Error',
            'message': str(error)
        }), HTTP_BAD_REQUEST
    
    @app.errorhandler(404)
    def handle_not_found(error):
        """Handle 404 Not Found errors"""
        logger.info(f"Not found: {error}")
        return jsonify({
            'error': 'Not Found',
            'message': 'The requested resource was not found'
        }), HTTP_NOT_FOUND
    
    @app.errorhandler(400)
    def handle_bad_request(error):
        """Handle 400 Bad Request errors"""
        logger.warning(f"Bad request: {error}")
        return jsonify({
            'error': 'Bad Request',
            'message': 'The request could not be understood or was missing required parameters'
        }), HTTP_BAD_REQUEST
    
    @app.errorhandler(500)
    def handle_internal_error(error):
        """Handle 500 Internal Server errors"""
        logger.error(f"Internal server error: {error}", exc_info=True)
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred. Please try again later.'
        }), HTTP_INTERNAL_ERROR
    
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        """Handle all HTTP exceptions"""
        logger.warning(f"HTTP exception: {error}")
        return jsonify({
            'error': error.name,
            'message': error.description
        }), error.code
    
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        """Handle any unexpected errors"""
        logger.critical(f"Unexpected error: {error}", exc_info=True)
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred. Please try again later.'
        }), HTTP_INTERNAL_ERROR
