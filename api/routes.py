"""
API Routes for E-Commerce Recommendation System
Routes organized using Flask Blueprints
"""

from flask import Blueprint, request, jsonify
from services.recommendation_service import RecommendationService
from validators.validators import ValidationError
from config.constants import (
    HTTP_OK, HTTP_CREATED, HTTP_BAD_REQUEST, HTTP_INTERNAL_ERROR
)
import logging

# Create blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Initialize service
recommendation_service = RecommendationService()

# Setup logger
logger = logging.getLogger(__name__)


@api_bp.route('/recommendations/<string:user_id>', methods=['GET'])
def get_recommendations(user_id):
    """
    Get personalized recommendations for a user
    ---
    tags:
      - Recommendations
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: Unique identifier for the user
        example: "user123"
      - name: limit
        in: query
        type: integer
        required: false
        default: 5
        description: Maximum number of recommendations to return (1-50)
        example: 10
    responses:
      200:
        description: Successful response with recommendations
        schema:
          type: object
          properties:
            user_id:
              type: string
              example: "user123"
            recommendations:
              type: array
              items:
                type: object
                properties:
                  product_id:
                    type: string
                    example: "P001"
                  name:
                    type: string
                    example: "Wireless Bluetooth Headphones"
                  category:
                    type: string
                    example: "Electronics"
                  price:
                    type: number
                    format: float
                    example: 79.99
                  rating:
                    type: number
                    format: float
                    example: 4.5
                  similarity_score:
                    type: number
                    format: float
                    example: 0.92
            count:
              type: integer
              example: 5
      400:
        description: Bad request - validation error
        schema:
          type: object
          properties:
            error:
              type: string
              example: "User ID must be a non-empty string"
      500:
        description: Internal server error
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Internal server error"
    """
    try:
        limit = request.args.get('limit', default=5, type=int)
        result = recommendation_service.get_user_recommendations(user_id, limit)
        return jsonify(result), HTTP_OK
    
    except ValidationError as e:
        logger.warning(f"Validation error in get_recommendations: {str(e)}")
        return jsonify({'error': str(e)}), HTTP_BAD_REQUEST
    
    except Exception as e:
        logger.error(f"Error in get_recommendations: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), HTTP_INTERNAL_ERROR


@api_bp.route('/similar/<string:product_id>', methods=['GET'])
def get_similar(product_id):
    """
    Get similar products based on product ID
    ---
    tags:
      - Products
    parameters:
      - name: product_id
        in: path
        type: string
        required: true
        description: Unique identifier for the product
        example: "P001"
      - name: limit
        in: query
        type: integer
        required: false
        default: 5
        description: Maximum number of similar products to return (1-50)
        example: 5
    responses:
      200:
        description: List of similar products
        schema:
          type: object
          properties:
            product_id:
              type: string
              example: "P001"
            similar_products:
              type: array
              items:
                type: object
                properties:
                  product_id:
                    type: string
                    example: "P002"
                  name:
                    type: string
                    example: "Smart Fitness Watch"
                  category:
                    type: string
                    example: "Electronics"
                  price:
                    type: number
                    format: float
                    example: 129.99
                  rating:
                    type: number
                    format: float
                    example: 4.3
                  similarity_score:
                    type: number
                    format: float
                    example: 0.92
            count:
              type: integer
              example: 5
      400:
        description: Bad request - validation error
      500:
        description: Internal server error
    """
    try:
        limit = request.args.get('limit', default=5, type=int)
        result = recommendation_service.get_similar_products(product_id, limit)
        return jsonify(result), HTTP_OK
    
    except ValidationError as e:
        logger.warning(f"Validation error in get_similar: {str(e)}")
        return jsonify({'error': str(e)}), HTTP_BAD_REQUEST
    
    except Exception as e:
        logger.error(f"Error in get_similar: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), HTTP_INTERNAL_ERROR


@api_bp.route('/trending', methods=['GET'])
def get_trending():
    """
    Get trending products
    ---
    tags:
      - Products
    parameters:
      - name: limit
        in: query
        type: integer
        required: false
        default: 10
        description: Maximum number of trending products to return (1-100)
        example: 10
    responses:
      200:
        description: List of trending products
        schema:
          type: object
          properties:
            trending_products:
              type: array
              items:
                type: object
                properties:
                  product_id:
                    type: string
                    example: "P007"
                  name:
                    type: string
                    example: "Running Shoes"
                  category:
                    type: string
                    example: "Sports"
                  price:
                    type: number
                    format: float
                    example: 119.99
                  rating:
                    type: number
                    format: float
                    example: 4.7
                  views:
                    type: integer
                    example: 9876
                  purchases:
                    type: integer
                    example: 543
            count:
              type: integer
              example: 10
      400:
        description: Bad request - validation error
      500:
        description: Internal server error
    """
    try:
        limit = request.args.get('limit', default=10, type=int)
        result = recommendation_service.get_trending_products(limit)
        return jsonify(result), HTTP_OK
    
    except ValidationError as e:
        logger.warning(f"Validation error in get_trending: {str(e)}")
        return jsonify({'error': str(e)}), HTTP_BAD_REQUEST
    
    except Exception as e:
        logger.error(f"Error in get_trending: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), HTTP_INTERNAL_ERROR


@api_bp.route('/category/<string:category>', methods=['GET'])
def get_by_category(category):
    """
    Get products by category
    ---
    tags:
      - Products
    parameters:
      - name: category
        in: path
        type: string
        required: true
        description: Product category name
        enum: ["Electronics", "Clothing", "Books", "Home & Kitchen", "Sports"]
        example: "Electronics"
      - name: limit
        in: query
        type: integer
        required: false
        default: 10
        description: Maximum number of products to return (1-100)
        example: 10
    responses:
      200:
        description: List of products in the category
        schema:
          type: object
          properties:
            category:
              type: string
              example: "Electronics"
            products:
              type: array
              items:
                type: object
                properties:
                  product_id:
                    type: string
                    example: "P001"
                  name:
                    type: string
                    example: "Wireless Bluetooth Headphones"
                  category:
                    type: string
                    example: "Electronics"
                  price:
                    type: number
                    format: float
                    example: 79.99
                  rating:
                    type: number
                    format: float
                    example: 4.5
            count:
              type: integer
              example: 10
      400:
        description: Bad request - invalid category
      500:
        description: Internal server error
    """
    try:
        limit = request.args.get('limit', default=10, type=int)
        result = recommendation_service.get_products_by_category(category, limit)
        return jsonify(result), HTTP_OK
    
    except ValidationError as e:
        logger.warning(f"Validation error in get_by_category: {str(e)}")
        return jsonify({'error': str(e)}), HTTP_BAD_REQUEST
    
    except Exception as e:
        logger.error(f"Error in get_by_category: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), HTTP_INTERNAL_ERROR


@api_bp.route('/interaction', methods=['POST'])
def add_interaction():
    """
    Add user interaction
    ---
    tags:
      - Interactions
    parameters:
      - name: body
        in: body
        required: true
        description: User interaction data
        schema:
          type: object
          required:
            - user_id
            - product_id
          properties:
            user_id:
              type: string
              description: Unique identifier for the user
              example: "user123"
            product_id:
              type: string
              description: Unique identifier for the product
              example: "P001"
            interaction_type:
              type: string
              description: Type of user interaction
              enum: ["view", "purchase", "add_to_cart", "wishlist"]
              default: "view"
              example: "purchase"
            rating:
              type: number
              format: float
              description: User rating for the product (0.0 to 5.0)
              minimum: 0.0
              maximum: 5.0
              example: 4.5
    responses:
      201:
        description: Interaction recorded successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Interaction recorded successfully"
            user_id:
              type: string
              example: "user123"
            product_id:
              type: string
              example: "P001"
            interaction_type:
              type: string
              example: "purchase"
      400:
        description: Bad request - validation error
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Missing required field: user_id"
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body is required'}), HTTP_BAD_REQUEST
        
        result = recommendation_service.add_user_interaction(
            user_id=data.get('user_id'),
            product_id=data.get('product_id'),
            interaction_type=data.get('interaction_type', 'view'),
            rating=data.get('rating')
        )
        
        return jsonify(result), HTTP_CREATED
    
    except ValidationError as e:
        logger.warning(f"Validation error in add_interaction: {str(e)}")
        return jsonify({'error': str(e)}), HTTP_BAD_REQUEST
    
    except Exception as e:
        logger.error(f"Error in add_interaction: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), HTTP_INTERNAL_ERROR


@api_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    ---
    tags:
      - Health
    responses:
      200:
        description: API is healthy and running
        schema:
          type: object
          properties:
            status:
              type: string
              example: "healthy"
            service:
              type: string
              example: "E-Commerce Recommendation API"
            version:
              type: string
              example: "v1"
    """
    return jsonify({
        'status': 'healthy',
        'service': 'E-Commerce Recommendation API',
        'version': 'v1'
    }), HTTP_OK
