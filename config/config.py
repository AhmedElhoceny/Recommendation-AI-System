"""
Configuration module for the E-Commerce Recommendation System
Handles different environment configurations (development, testing, production)
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-this')
    DEBUG = False
    TESTING = False
    
    # API Configuration
    API_VERSION = 'v1'
    API_TITLE = 'E-Commerce Recommendation API'
    API_DESCRIPTION = 'Intelligent product recommendation system'
    
    # Pagination
    DEFAULT_PAGE_SIZE = 10
    MAX_PAGE_SIZE = 100
    
    # Recommendation Settings
    DEFAULT_RECOMMENDATIONS_LIMIT = 5
    MAX_RECOMMENDATIONS_LIMIT = 50
    
    # Data paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    PRODUCTS_FILE = os.path.join(DATA_DIR, 'sample_products.csv')
    
    # CORS
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    
    # Server
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    ENV = 'production'
    
    # Override with stronger settings for production
    SECRET_KEY = os.getenv('SECRET_KEY')  # Must be set in production
    
    @classmethod
    def validate(cls):
        """Validate production configuration"""
        if not cls.SECRET_KEY or cls.SECRET_KEY == 'dev-secret-key-change-this':
            raise ValueError("SECRET_KEY must be set for production")


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    ENV = 'testing'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env=None):
    """Get configuration based on environment"""
    if env is None:
        env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])
