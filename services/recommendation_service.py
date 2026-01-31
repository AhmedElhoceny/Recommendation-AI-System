"""
Service Layer for Recommendation Engine
Business logic separated from API routes
"""

from typing import List, Dict, Any, Optional
from models.recommendation_engine import RecommendationEngine
from validators.validators import Validator, ValidationError
from config.config import Config


class RecommendationService:
    """
    Service layer for recommendation operations
    Handles business logic and orchestration
    """
    
    def __init__(self):
        self.engine = RecommendationEngine()
        self.validator = Validator()
    
    def get_user_recommendations(
        self, 
        user_id: str, 
        limit: int = Config.DEFAULT_RECOMMENDATIONS_LIMIT
    ) -> Dict[str, Any]:
        """
        Get personalized recommendations for a user
        
        Args:
            user_id: User identifier
            limit: Number of recommendations
            
        Returns:
            Dictionary with recommendations
            
        Raises:
            ValidationError: If validation fails
        """
        # Validate inputs
        self.validator.validate_user_id(user_id)
        limit = self.validator.validate_limit(limit, Config.MAX_RECOMMENDATIONS_LIMIT)
        
        # Get recommendations from engine
        recommendations = self.engine.get_recommendations_for_user(user_id, limit)
        
        return {
            'user_id': user_id,
            'recommendations': recommendations,
            'count': len(recommendations)
        }
    
    def get_similar_products(
        self, 
        product_id: str, 
        limit: int = Config.DEFAULT_RECOMMENDATIONS_LIMIT
    ) -> Dict[str, Any]:
        """
        Get similar products
        
        Args:
            product_id: Product identifier
            limit: Number of similar products
            
        Returns:
            Dictionary with similar products
            
        Raises:
            ValidationError: If validation fails
        """
        # Validate inputs
        self.validator.validate_product_id(product_id)
        limit = self.validator.validate_limit(limit, Config.MAX_RECOMMENDATIONS_LIMIT)
        
        # Get similar products from engine
        similar_products = self.engine.get_similar_products(product_id, limit)
        
        return {
            'product_id': product_id,
            'similar_products': similar_products,
            'count': len(similar_products)
        }
    
    def get_trending_products(
        self, 
        limit: int = Config.DEFAULT_PAGE_SIZE
    ) -> Dict[str, Any]:
        """
        Get trending products
        
        Args:
            limit: Number of products
            
        Returns:
            Dictionary with trending products
            
        Raises:
            ValidationError: If validation fails
        """
        # Validate inputs
        limit = self.validator.validate_limit(limit, Config.MAX_PAGE_SIZE)
        
        # Get trending products from engine
        trending = self.engine.get_trending_products(limit)
        
        return {
            'trending_products': trending,
            'count': len(trending)
        }
    
    def get_products_by_category(
        self, 
        category: str, 
        limit: int = Config.DEFAULT_PAGE_SIZE
    ) -> Dict[str, Any]:
        """
        Get products by category
        
        Args:
            category: Product category
            limit: Number of products
            
        Returns:
            Dictionary with products
            
        Raises:
            ValidationError: If validation fails
        """
        # Validate inputs
        self.validator.validate_category(category)
        limit = self.validator.validate_limit(limit, Config.MAX_PAGE_SIZE)
        
        # Get products from engine
        products = self.engine.get_products_by_category(category, limit)
        
        return {
            'category': category,
            'products': products,
            'count': len(products)
        }
    
    def add_user_interaction(
        self, 
        user_id: str, 
        product_id: str,
        interaction_type: str = 'view',
        rating: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Record user interaction
        
        Args:
            user_id: User identifier
            product_id: Product identifier
            interaction_type: Type of interaction
            rating: Optional rating
            
        Returns:
            Success confirmation
            
        Raises:
            ValidationError: If validation fails
        """
        # Validate inputs
        payload = {
            'user_id': user_id,
            'product_id': product_id,
            'interaction_type': interaction_type,
            'rating': rating
        }
        validated_data = self.validator.validate_interaction_payload(payload)
        
        # Add interaction through engine
        self.engine.add_user_interaction(
            validated_data['user_id'],
            validated_data['product_id'],
            validated_data['interaction_type'],
            validated_data['rating']
        )
        
        return {
            'message': 'Interaction recorded successfully',
            'user_id': validated_data['user_id'],
            'product_id': validated_data['product_id'],
            'interaction_type': validated_data['interaction_type']
        }
