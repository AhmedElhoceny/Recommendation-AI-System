"""
Validators for E-Commerce Recommendation System
Input validation logic separated from business logic
"""

import re
from typing import Optional, Dict, Any
from config.constants import (
    VALID_INTERACTION_TYPES,
    VALID_CATEGORIES,
    MIN_RATING,
    MAX_RATING,
    USER_ID_MIN_LENGTH,
    USER_ID_MAX_LENGTH
)


class ValidationError(Exception):
    """Custom validation error"""
    pass


class Validator:
    """Input validation class"""
    
    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        """
        Validate user ID
        
        Args:
            user_id: User identifier
            
        Returns:
            True if valid
            
        Raises:
            ValidationError: If validation fails
        """
        if not user_id or not isinstance(user_id, str):
            raise ValidationError("User ID must be a non-empty string")
        
        if len(user_id) < USER_ID_MIN_LENGTH or len(user_id) > USER_ID_MAX_LENGTH:
            raise ValidationError(
                f"User ID must be between {USER_ID_MIN_LENGTH} and {USER_ID_MAX_LENGTH} characters"
            )
        
        return True
    
    @staticmethod
    def validate_product_id(product_id: str) -> bool:
        """
        Validate product ID
        
        Args:
            product_id: Product identifier
            
        Returns:
            True if valid
            
        Raises:
            ValidationError: If validation fails
        """
        if not product_id or not isinstance(product_id, str):
            raise ValidationError("Product ID must be a non-empty string")
        
        if len(product_id) < 1:
            raise ValidationError("Product ID cannot be empty")
        
        return True
    
    @staticmethod
    def validate_rating(rating: Optional[float]) -> bool:
        """
        Validate rating value
        
        Args:
            rating: Rating value
            
        Returns:
            True if valid
            
        Raises:
            ValidationError: If validation fails
        """
        if rating is None:
            return True
        
        try:
            rating_float = float(rating)
        except (ValueError, TypeError):
            raise ValidationError("Rating must be a number")
        
        if not MIN_RATING <= rating_float <= MAX_RATING:
            raise ValidationError(f"Rating must be between {MIN_RATING} and {MAX_RATING}")
        
        return True
    
    @staticmethod
    def validate_limit(limit: int, max_limit: int = 50) -> int:
        """
        Validate and sanitize limit parameter
        
        Args:
            limit: Requested limit
            max_limit: Maximum allowed limit
            
        Returns:
            Validated limit value
            
        Raises:
            ValidationError: If validation fails
        """
        try:
            limit_int = int(limit)
        except (ValueError, TypeError):
            raise ValidationError("Limit must be an integer")
        
        if limit_int < 1:
            raise ValidationError("Limit must be at least 1")
        
        if limit_int > max_limit:
            limit_int = max_limit
        
        return limit_int
    
    @staticmethod
    def validate_interaction_type(interaction_type: str) -> bool:
        """
        Validate interaction type
        
        Args:
            interaction_type: Type of interaction
            
        Returns:
            True if valid
            
        Raises:
            ValidationError: If validation fails
        """
        if not interaction_type or not isinstance(interaction_type, str):
            raise ValidationError("Interaction type must be a non-empty string")
        
        if interaction_type not in VALID_INTERACTION_TYPES:
            raise ValidationError(
                f"Invalid interaction type. Must be one of: {', '.join(VALID_INTERACTION_TYPES)}"
            )
        
        return True
    
    @staticmethod
    def validate_category(category: str) -> bool:
        """
        Validate category
        
        Args:
            category: Product category
            
        Returns:
            True if valid
            
        Raises:
            ValidationError: If validation fails
        """
        if not category or not isinstance(category, str):
            raise ValidationError("Category must be a non-empty string")
        
        # Case-insensitive validation
        category_lower = category.lower()
        valid_categories_lower = [cat.lower() for cat in VALID_CATEGORIES]
        
        if category_lower not in valid_categories_lower:
            raise ValidationError(
                f"Invalid category. Must be one of: {', '.join(VALID_CATEGORIES)}"
            )
        
        return True
    
    @staticmethod
    def validate_interaction_payload(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate interaction payload
        
        Args:
            data: Request payload
            
        Returns:
            Validated and sanitized data
            
        Raises:
            ValidationError: If validation fails
        """
        if not data:
            raise ValidationError("Request body is required")
        
        # Required fields
        if 'user_id' not in data:
            raise ValidationError("Missing required field: user_id")
        
        if 'product_id' not in data:
            raise ValidationError("Missing required field: product_id")
        
        # Validate each field
        Validator.validate_user_id(data['user_id'])
        Validator.validate_product_id(data['product_id'])
        
        # Optional fields with defaults
        interaction_type = data.get('interaction_type', 'view')
        Validator.validate_interaction_type(interaction_type)
        
        rating = data.get('rating')
        if rating is not None:
            Validator.validate_rating(rating)
        
        return {
            'user_id': data['user_id'],
            'product_id': data['product_id'],
            'interaction_type': interaction_type,
            'rating': rating
        }
