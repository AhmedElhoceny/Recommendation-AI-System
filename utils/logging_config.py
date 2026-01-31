"""
Logging configuration for E-Commerce Recommendation System
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime


def setup_logging(app):
    """
    Configure logging for the application
    
    Args:
        app: Flask application instance
    """
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(app.config['BASE_DIR'], 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Set log level based on environment
    log_level = logging.DEBUG if app.config['DEBUG'] else logging.INFO
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    
    # File handler for all logs
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, 'app.log'),
        maxBytes=10240000,  # 10MB
        backupCount=10
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(detailed_formatter)
    
    # File handler for errors only
    error_file_handler = RotatingFileHandler(
        os.path.join(log_dir, 'error.log'),
        maxBytes=10240000,  # 10MB
        backupCount=10
    )
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(detailed_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(detailed_formatter)
    
    # Configure app logger
    app.logger.setLevel(log_level)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(error_file_handler)
    app.logger.addHandler(console_handler)
    
    # Configure root logger
    logging.getLogger().setLevel(log_level)
    logging.getLogger().addHandler(file_handler)
    logging.getLogger().addHandler(error_file_handler)
    
    app.logger.info(f"Logging configured - Level: {logging.getLevelName(log_level)}")
