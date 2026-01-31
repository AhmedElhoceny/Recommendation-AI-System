"""
Unit Tests for Validators
"""

import unittest
from validators.validators import Validator, ValidationError


class TestValidators(unittest.TestCase):
    """Test validation functions"""
    
    def setUp(self):
        self.validator = Validator()
    
    def test_validate_user_id_valid(self):
        """Test valid user ID"""
        self.assertTrue(self.validator.validate_user_id("user123"))
    
    def test_validate_user_id_empty(self):
        """Test empty user ID"""
        with self.assertRaises(ValidationError):
            self.validator.validate_user_id("")
    
    def test_validate_user_id_none(self):
        """Test None user ID"""
        with self.assertRaises(ValidationError):
            self.validator.validate_user_id(None)
    
    def test_validate_product_id_valid(self):
        """Test valid product ID"""
        self.assertTrue(self.validator.validate_product_id("P001"))
    
    def test_validate_product_id_empty(self):
        """Test empty product ID"""
        with self.assertRaises(ValidationError):
            self.validator.validate_product_id("")
    
    def test_validate_rating_valid(self):
        """Test valid rating"""
        self.assertTrue(self.validator.validate_rating(4.5))
    
    def test_validate_rating_out_of_range(self):
        """Test rating out of range"""
        with self.assertRaises(ValidationError):
            self.validator.validate_rating(6.0)
    
    def test_validate_rating_none(self):
        """Test None rating (should be valid)"""
        self.assertTrue(self.validator.validate_rating(None))
    
    def test_validate_limit_valid(self):
        """Test valid limit"""
        result = self.validator.validate_limit(10)
        self.assertEqual(result, 10)
    
    def test_validate_limit_exceeds_max(self):
        """Test limit exceeds max"""
        result = self.validator.validate_limit(100, max_limit=50)
        self.assertEqual(result, 50)
    
    def test_validate_limit_negative(self):
        """Test negative limit"""
        with self.assertRaises(ValidationError):
            self.validator.validate_limit(-1)
    
    def test_validate_interaction_type_valid(self):
        """Test valid interaction type"""
        self.assertTrue(self.validator.validate_interaction_type("view"))
    
    def test_validate_interaction_type_invalid(self):
        """Test invalid interaction type"""
        with self.assertRaises(ValidationError):
            self.validator.validate_interaction_type("invalid_type")
    
    def test_validate_category_valid(self):
        """Test valid category"""
        self.assertTrue(self.validator.validate_category("Electronics"))
    
    def test_validate_category_case_insensitive(self):
        """Test category validation is case insensitive"""
        self.assertTrue(self.validator.validate_category("electronics"))
    
    def test_validate_category_invalid(self):
        """Test invalid category"""
        with self.assertRaises(ValidationError):
            self.validator.validate_category("InvalidCategory")
    
    def test_validate_interaction_payload_complete(self):
        """Test complete interaction payload"""
        payload = {
            'user_id': 'user123',
            'product_id': 'P001',
            'interaction_type': 'purchase',
            'rating': 4.5
        }
        result = self.validator.validate_interaction_payload(payload)
        self.assertEqual(result['user_id'], 'user123')
        self.assertEqual(result['product_id'], 'P001')
        self.assertEqual(result['interaction_type'], 'purchase')
        self.assertEqual(result['rating'], 4.5)
    
    def test_validate_interaction_payload_missing_required(self):
        """Test interaction payload missing required fields"""
        payload = {'user_id': 'user123'}
        with self.assertRaises(ValidationError):
            self.validator.validate_interaction_payload(payload)


if __name__ == '__main__':
    unittest.main()
