"""
Test script for E-Commerce Recommendation API
Run this after starting the Flask server to test all endpoints
"""

import requests
import json

BASE_URL = "http://localhost:5000/api/v1"


def test_health_check():
    """Test health check endpoint"""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_trending_products():
    """Test trending products endpoint"""
    print("\n=== Testing Trending Products ===")
    response = requests.get(f"{BASE_URL}/trending?limit=5")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_similar_products():
    """Test similar products endpoint"""
    print("\n=== Testing Similar Products ===")
    response = requests.get(f"{BASE_URL}/similar/P001?limit=5")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_category_products():
    """Test category products endpoint"""
    print("\n=== Testing Category Products ===")
    response = requests.get(f"{BASE_URL}/category/Electronics?limit=5")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_add_interaction():
    """Test add interaction endpoint"""
    print("\n=== Testing Add User Interaction ===")
    interaction_data = {
        'user_id': 'test_user_001',
        'product_id': 'P001',
        'interaction_type': 'view',
        'rating': 4.5
    }
    response = requests.post(
        f"{BASE_URL}/interaction",
        json=interaction_data
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_user_recommendations():
    """Test user recommendations endpoint"""
    print("\n=== Testing User Recommendations ===")
    response = requests.get(f"{BASE_URL}/recommendations/test_user_001?limit=5")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def run_all_tests():
    """Run all API tests"""
    print("=" * 60)
    print("Starting API Tests...")
    print("Make sure the Flask server is running on http://localhost:5000")
    print("=" * 60)
    
    try:
        test_health_check()
        test_trending_products()
        test_similar_products()
        test_category_products()
        test_add_interaction()
        test_user_recommendations()
        
        print("\n" + "=" * 60)
        print("✅ All Tests Completed Successfully!")
        print("=" * 60)
    except requests.exceptions.ConnectionError:
        print("\n" + "=" * 60)
        print("❌ Error: Could not connect to the server.")
        print("Please make sure the Flask server is running on http://localhost:5000")
        print("=" * 60)
    except Exception as e:
        print(f"\n❌ Error during testing: {str(e)}")


if __name__ == "__main__":
    run_all_tests()
