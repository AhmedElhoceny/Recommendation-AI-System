import json
from datetime import datetime


def format_response(data, status='success', message=None):
    """
    Format API response consistently
    
    Args:
        data: Response data
        status: Response status (success/error)
        message: Optional message
    
    Returns:
        Formatted response dictionary
    """
    response = {
        'status': status,
        'timestamp': datetime.now().isoformat(),
        'data': data
    }
    
    if message:
        response['message'] = message
    
    return response


def validate_user_id(user_id):
    """Validate user ID format"""
    if not user_id or not isinstance(user_id, str):
        return False
    return len(user_id) > 0


def validate_product_id(product_id):
    """Validate product ID format"""
    if not product_id or not isinstance(product_id, str):
        return False
    return len(product_id) > 0


def validate_rating(rating):
    """Validate rating value"""
    if rating is None:
        return True
    try:
        rating_float = float(rating)
        return 0 <= rating_float <= 5
    except (ValueError, TypeError):
        return False


def log_api_call(endpoint, method, user_id=None):
    """Log API call for monitoring"""
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'endpoint': endpoint,
        'method': method,
        'user_id': user_id
    }
    # In production, send to logging service
    print(f"API Call: {json.dumps(log_entry)}")
