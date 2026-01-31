"""
Swagger/OpenAPI Configuration for E-Commerce Recommendation API
"""

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "E-Commerce Recommendation API",
        "description": "Intelligent product recommendation system with multiple recommendation strategies including collaborative filtering, content-based filtering, and trending algorithms.",
        "contact": {
            "name": "API Support",
            "email": "support@ecommerce-api.com"
        },
        "version": "1.0.0"
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "tags": [
        {
            "name": "Health",
            "description": "Health check endpoints"
        },
        {
            "name": "Recommendations",
            "description": "Personalized product recommendations"
        },
        {
            "name": "Products",
            "description": "Product discovery and search"
        },
        {
            "name": "Interactions",
            "description": "User interaction tracking"
        }
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
        }
    }
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
    "title": "E-Commerce Recommendation API",
    "version": "1.0.0",
    "description": "Interactive API documentation for E-Commerce Recommendation System",
    "termsOfService": "",
    "hide_top_bar": False,
}
