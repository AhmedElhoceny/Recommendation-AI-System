import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
import os


class RecommendationEngine:
    """
    E-Commerce Recommendation Engine
    Implements multiple recommendation strategies:
    - Collaborative Filtering
    - Content-Based Filtering
    - Trending Products
    """
    
    def __init__(self):
        self.products_df = None
        self.interactions_df = None
        self.user_product_matrix = None
        self.product_similarity_matrix = None
        self.load_data()
        self.initialize_models()
    
    def load_data(self):
        """Load product and interaction data"""
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        
        # Load or create sample product data
        products_file = os.path.join(data_dir, 'sample_products.csv')
        if os.path.exists(products_file):
            self.products_df = pd.read_csv(products_file)
        else:
            self.products_df = self._create_sample_products()
        
        # Initialize empty interactions dataframe
        self.interactions_df = pd.DataFrame(columns=[
            'user_id', 'product_id', 'interaction_type', 'rating', 'timestamp'
        ])
    
    def _create_sample_products(self):
        """Create sample product data"""
        products = {
            'product_id': [f'P{str(i).zfill(3)}' for i in range(1, 51)],
            'name': [f'Product {i}' for i in range(1, 51)],
            'category': np.random.choice(
                ['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Sports'],
                50
            ),
            'price': np.random.uniform(10, 500, 50).round(2),
            'rating': np.random.uniform(3.0, 5.0, 50).round(1),
            'views': np.random.randint(100, 10000, 50),
            'purchases': np.random.randint(10, 1000, 50)
        }
        return pd.DataFrame(products)
    
    def initialize_models(self):
        """Initialize recommendation models"""
        # Create product similarity matrix based on categories and ratings
        if not self.products_df.empty:
            self._compute_product_similarity()
    
    def _compute_product_similarity(self):
        """Compute product similarity based on features"""
        # One-hot encode categories
        category_dummies = pd.get_dummies(self.products_df['category'])
        
        # Normalize numerical features
        scaler = MinMaxScaler()
        numerical_features = self.products_df[['price', 'rating']].values
        normalized_features = scaler.fit_transform(numerical_features)
        
        # Combine features
        features = np.hstack([category_dummies.values, normalized_features])
        
        # Compute cosine similarity
        self.product_similarity_matrix = cosine_similarity(features)
    
    def get_recommendations_for_user(self, user_id, limit=5):
        """
        Get personalized recommendations for a user
        Uses collaborative filtering if user has interactions, 
        otherwise returns trending products
        """
        user_interactions = self.interactions_df[
            self.interactions_df['user_id'] == user_id
        ]
        
        if user_interactions.empty:
            # New user - return trending products
            return self.get_trending_products(limit)
        
        # Get products user has interacted with
        interacted_products = set(user_interactions['product_id'].tolist())
        
        # Get similar products based on user's interactions
        recommendations = []
        for product_id in interacted_products:
            similar = self.get_similar_products(product_id, limit=10)
            recommendations.extend(similar)
        
        # Filter out already interacted products and get top N
        recommendations = [
            rec for rec in recommendations 
            if rec['product_id'] not in interacted_products
        ]
        
        # Remove duplicates and sort by score
        seen = set()
        unique_recommendations = []
        for rec in recommendations:
            if rec['product_id'] not in seen:
                seen.add(rec['product_id'])
                unique_recommendations.append(rec)
        
        return unique_recommendations[:limit]
    
    def get_similar_products(self, product_id, limit=5):
        """Get similar products based on content-based filtering"""
        if self.products_df.empty or self.product_similarity_matrix is None:
            return []
        
        try:
            # Find product index
            product_idx = self.products_df[
                self.products_df['product_id'] == product_id
            ].index[0]
            
            # Get similarity scores
            similarity_scores = list(enumerate(
                self.product_similarity_matrix[product_idx]
            ))
            
            # Sort by similarity (excluding the product itself)
            similarity_scores = sorted(
                similarity_scores, 
                key=lambda x: x[1], 
                reverse=True
            )[1:limit+1]
            
            # Get similar products
            similar_products = []
            for idx, score in similarity_scores:
                product = self.products_df.iloc[idx]
                similar_products.append({
                    'product_id': product['product_id'],
                    'name': product['name'],
                    'category': product['category'],
                    'price': float(product['price']),
                    'rating': float(product['rating']),
                    'similarity_score': float(score)
                })
            
            return similar_products
        except (IndexError, KeyError):
            return []
    
    def get_trending_products(self, limit=10):
        """Get trending products based on views and purchases"""
        if self.products_df.empty:
            return []
        
        # Calculate trending score
        df = self.products_df.copy()
        df['trending_score'] = (
            df['views'] * 0.3 + 
            df['purchases'] * 0.5 + 
            df['rating'] * 100 * 0.2
        )
        
        # Sort by trending score
        trending = df.nlargest(limit, 'trending_score')
        
        return [
            {
                'product_id': row['product_id'],
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
                'rating': float(row['rating']),
                'views': int(row['views']),
                'purchases': int(row['purchases'])
            }
            for _, row in trending.iterrows()
        ]
    
    def get_products_by_category(self, category, limit=10):
        """Get products by category"""
        if self.products_df.empty:
            return []
        
        category_products = self.products_df[
            self.products_df['category'].str.lower() == category.lower()
        ]
        
        # Sort by rating
        category_products = category_products.nlargest(limit, 'rating')
        
        return [
            {
                'product_id': row['product_id'],
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
                'rating': float(row['rating'])
            }
            for _, row in category_products.iterrows()
        ]
    
    def add_user_interaction(self, user_id, product_id, 
                            interaction_type='view', rating=None):
        """Add user interaction to the system"""
        new_interaction = {
            'user_id': user_id,
            'product_id': product_id,
            'interaction_type': interaction_type,
            'rating': rating,
            'timestamp': datetime.now().isoformat()
        }
        
        self.interactions_df = pd.concat([
            self.interactions_df,
            pd.DataFrame([new_interaction])
        ], ignore_index=True)
        
        return True
