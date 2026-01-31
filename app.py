"""
E-Commerce Recommendation System - Main Application
Flask REST API with Factory Pattern and Clean Architecture
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
import os
import logging

from config.config import get_config
from api.routes import api_bp
from api.error_handlers import register_error_handlers
from utils.logging_config import setup_logging
from config.swagger_config import swagger_config, swagger_template


def create_app(config_name=None):
    """
    Application Factory Pattern
    Creates and configures the Flask application
    
    Args:
        config_name: Configuration environment name
        
    Returns:
        Configured Flask application instance
    """
    # Create Flask app
    app = Flask(__name__)
    
    # Load configuration
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    config_class = get_config(config_name)
    app.config.from_object(config_class)
    
    # Setup logging
    setup_logging(app)
    
    # Initialize CORS
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # Initialize Swagger
    Swagger(app, config=swagger_config, template=swagger_template)
    
    # Register blueprints
    app.register_blueprint(api_bp)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Root endpoint
    @app.route('/')
    def index():
        return jsonify({
            'service': app.config['API_TITLE'],
            'description': app.config['API_DESCRIPTION'],
            'version': app.config['API_VERSION'],
            'status': 'running'
        })
    
    # Legacy health endpoint for backward compatibility
    @app.route('/health')
    def health():
        return jsonify({
            'status': 'healthy',
            'message': 'E-Commerce Recommendation API is running'
        })
    
    app.logger.info(f"Application created with config: {config_name}")
    return app


# Create app instance
app = create_app()


if __name__ == '__main__':
    port = app.config['PORT']
    host = app.config['HOST']
    debug = app.config['DEBUG']
    
    app.logger.info(f"Starting {app.config['API_TITLE']} on {host}:{port}")
    app.logger.info(f"Environment: {app.config['ENV']}")
    app.logger.info(f"Debug mode: {debug}")
    
    app.run(host=host, port=port, debug=debug)
