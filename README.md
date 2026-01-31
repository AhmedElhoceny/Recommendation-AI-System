# E-Commerce Recommendation System API

A production-ready Flask REST API for an intelligent e-commerce recommendation system with clean architecture, implementing personalized product recommendations, similar products discovery, and trending items analysis.

## 🏗️ Architecture

This project follows **Clean Architecture** principles with clear separation of concerns:

### Layered Architecture

```
┌─────────────────────────────────────────┐
│         API Layer (Routes)              │  ← HTTP endpoints, request handling
├─────────────────────────────────────────┤
│      Service Layer (Business Logic)     │  ← Business rules, orchestration
├─────────────────────────────────────────┤
│     Models Layer (ML Algorithms)        │  ← Recommendation engine, ML models
├─────────────────────────────────────────┤
│     Data Layer (Data Access)            │  ← Data loading, persistence
└─────────────────────────────────────────┘
```

### Design Patterns

- **Factory Pattern**: Application creation with configurable environments
- **Service Layer Pattern**: Business logic separation from routes
- **Repository Pattern**: Data access abstraction
- **Blueprint Pattern**: Modular route organization
- **Dependency Injection**: Loose coupling between components

## 📁 Project Structure

```
E-Commerce Recommendation System/
├── app.py                          # Application factory and entry point
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables
├── .gitignore                     # Git ignore rules
├── README.md                      # Documentation
│
├── api/                           # API Layer
│   ├── __init__.py
│   ├── routes.py                  # API endpoints (Blueprints)
│   └── error_handlers.py          # Centralized error handling
│
├── services/                      # Service Layer
│   ├── __init__.py
│   └── recommendation_service.py  # Business logic
│
├── models/                        # Models Layer
│   ├── __init__.py
│   └── recommendation_engine.py   # ML recommendation algorithms
│
├── validators/                    # Validation Layer
│   ├── __init__.py
│   └── validators.py              # Input validation logic
│
├── config/                        # Configuration
│   ├── __init__.py
│   ├── config.py                  # Environment configurations
│   └── constants.py               # Application constants
│
├── utils/                         # Utilities
│   ├── __init__.py
│   ├── helpers.py                 # Helper functions
│   └── logging_config.py          # Logging configuration
│
├── data/                          # Data Layer
│   └── sample_products.csv        # Sample product data
│
├── tests/                         # Test Suite
│   ├── __init__.py
│   └── test_validators.py         # Unit tests
│
└── logs/                          # Application logs (auto-generated)
    ├── app.log                    # General logs
    └── error.log                  # Error logs
```

## ✨ Features

- **Personalized Recommendations**: ML-powered product suggestions based on user interaction history
- **Similar Products**: Content-based filtering using cosine similarity
- **Trending Products**: Discover popular items based on views, purchases, and ratings
- **Category-based Search**: Browse products by category
- **User Interaction Tracking**: Record views, purchases, wishlist additions
- **Input Validation**: Comprehensive validation with detailed error messages
- **Structured Logging**: Rotating file logs with multiple log levels
- **Error Handling**: Centralized error handling with consistent API responses
- **API Versioning**: Version-controlled endpoints (`/api/v1/`)
- **CORS Support**: Cross-origin resource sharing enabled
- **Swagger/OpenAPI**: Interactive API documentation with Swagger UI

## 🛠️ Tech Stack

- **Flask**: Lightweight web framework
- **Flasgger**: Swagger/OpenAPI documentation
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning (cosine similarity, preprocessing)
- **Flask-CORS**: Cross-origin resource sharing
- **Python-dotenv**: Environment variable management
- **Gunicorn**: Production WSGI server

## 📦 Installation

1. **Clone the repository**:
```bash
cd "c:\Self Study\ML\E-Commerce Recommendation System"
```

2. **Create a virtual environment**:
```bash
python -m venv venv
```

3. **Activate the virtual environment**:
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

5. **Configure environment variables**:
   - Edit `.env` file and update values as needed
   - Set `SECRET_KEY` to a secure random string in production
   - Configure `FLASK_ENV` (development/production/testing)

## 🚀 Running the Application

### Development Mode

```bash
python app.py
```

The API will start on `http://localhost:5000`

### Production Mode

```bash
# Using Gunicorn (recommended)
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"

# With specific environment
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app('production')"
```

### Testing

```bash
# Run unit tests
python -m unittest discover tests

# Run specific test
python -m unittest tests.test_validators
```

## 📍 API Endpoints

### Base URL
```
http://localhost:5000/api/v1
```

### 📚 Interactive API Documentation

**Swagger UI is available at:** `http://localhost:5000/swagger/`

The Swagger interface provides:
- ✅ Interactive endpoint testing
- ✅ Request/response examples
- ✅ Schema definitions
- ✅ Try it out functionality

### Health Check

**GET** `/api/v1/health`

Check if the API is running.

**Response**:
```json
{
  "status": "healthy",
  "service": "E-Commerce Recommendation API",
  "version": "v1"
}
```

### Get User Recommendations

**GET** `/api/v1/recommendations/<user_id>?limit=5`

Get personalized product recommendations for a user.

**Parameters**:
- `user_id` (path): User identifier
- `limit` (query, optional): Number of recommendations (default: 5)

**Response**:
```json
{
  "user_id": "user123",
  "recommendations": [
    {
      "product_id": "P001",
      "name": "Wireless Bluetooth Headphones",
      "category": "Electronics",
      "price": 79.99,
      "rating": 4.5,
      "similarity_score": 0.85
    }
  ],
  "count": 5
}
```

### Get Similar Products

**GET** `/api/v1/similar/<product_id>?limit=5`

Find products similar to a given product.

**Parameters**:
- `product_id` (path): Product identifier
- `limit` (query, optional): Number of similar products (default: 5)

**Response**:
```json
{
  "product_id": "P001",
  "similar_products": [
    {
      "product_id": "P002",
      "name": "Smart Fitness Watch",
      "category": "Electronics",
      "price": 129.99,
      "rating": 4.3,
      "similarity_score": 0.92
    }
  ],
  "count": 5
}
```

### Get Trending Products

**GET** `/api/v1/trending?limit=10`

Get currently trending products.

**Parameters**:
- `limit` (query, optional): Number of trending products (default: 10)

**Response**:
```json
{
  "trending_products": [
    {
      "product_id": "P007",
      "name": "Running Shoes",
      "category": "Sports",
      "price": 119.99,
      "rating": 4.7,
      "views": 9876,
      "purchases": 543
    }
  ],
  "count": 10
}
```

### Get Products by Category

**GET** `/api/v1/category/<category>?limit=10`

Get products in a specific category.

**Parameters**:
- `category` (path): Category name (Electronics, Clothing, Books, Home & Kitchen, Sports)
- `limit` (query, optional): Number of products (default: 10)

**Response**:
```json
{
  "category": "Electronics",
  "products": [
    {
      "product_id": "P001",
      "name": "Wireless Bluetooth Headphones",
      "category": "Electronics",
      "price": 79.99,
      "rating": 4.5
    }
  ],
  "count": 10
}
```

### Add User Interaction

**POST** `/api/v1/interaction`

Record a user interaction with a product.

**Request Body**:
```json
{
  "user_id": "user123",
  "product_id": "P001",
  "interaction_type": "view",
  "rating": 4.5
}
```

**Response**:
```json
{
  "message": "Interaction recorded successfully",
  "user_id": "user123",
  "product_id": "P001",
  "interaction_type": "view"
}
```

## 🧪 Example Usage

### Using cURL

```bash
# Get recommendations for a user
curl http://localhost:5000/api/v1/recommendations/user123?limit=5

# Find similar products
curl http://localhost:5000/api/v1/similar/P001?limit=5

# Get trending products
curl http://localhost:5000/api/v1/trending?limit=10

# Get products by category
curl http://localhost:5000/api/v1/category/Electronics?limit=10

# Add user interaction
curl -X POST http://localhost:5000/api/v1/interaction \
  -H "Content-Type: application/json" \
  -d '{"user_id":"user123","product_id":"P001","interaction_type":"purchase","rating":5}'
```

### Content-Based Filtering
- Uses product features (category, price, rating) to find similar products
- Computes cosine similarity between product feature vectors

### Collaborative Filtering
- Recommends products based on user interaction history
- Suggests items similar to what the user has previously interacted with

### Trending Algorithm
- Combines views, purchases, and ratings with weighted scoring
- Formula: `trending_score = views * 0.3 + purchases * 0.5 + rating * 100 * 0.2`

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
FLASK_ENV=development          # development, production, testing
SECRET_KEY=your-secret-key     # Change in production!
PORT=5000
HOST=0.0.0.0
CORS_ORIGINS=*                 # Configure for production
```

### Configuration Classes

The application supports multiple environments:

- **Development**: Debug mode enabled, verbose logging
- **Production**: Optimized for performance, requires SECRET_KEY
- **Testing**: Isolated testing environment

```python
# Create app with specific config
from app import create_app

app = create_app('production')
```

## 📊 Logging

Logs are automatically created in the `logs/` directory:

- `app.log`: All application logs (INFO and above)
- `error.log`: Error logs only (ERROR and above)

Log rotation is configured with:
- Max file size: 10MB
- Backup count: 10 files

## 🔒 Error Handling

The API provides consistent error responses:

```json
{
  "error": "Error Type",
  "message": "Detailed error message"
}
```

Common HTTP status codes:
- `200`: Success
- `201`: Created
- `400`: Bad Request (validation errors)
- `404`: Not Found
- `500`: Internal Server Error

## ✅ Input Validation

All endpoints validate input parameters:

- **User ID**: Non-empty string, 1-100 characters
- **Product ID**: Non-empty string
- **Rating**: Float between 0.0 and 5.0
- **Limit**: Integer between 1 and max limit
- **Category**: Must be one of: Electronics, Clothing, Books, Home & Kitchen, Sports
- **Interaction Type**: Must be: view, purchase, add_to_cart, wishlist

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m unittest discover tests

# Run with coverage
pip install coverage
coverage run -m unittest discover tests
coverage report
```

Sample test data includes 50 products across 5 categories.

## 📈 Performance Considerations

- **Caching**: Consider implementing Redis for frequently accessed data
- **Database**: For production, migrate from CSV to PostgreSQL/MongoDB
- **Async**: Use Celery for background tasks (model retraining, analytics)
- **Rate Limiting**: Implement Flask-Limiter for API rate limiting
- **Monitoring**: Add Prometheus metrics and Grafana dashboards

## 🚀 Deployment

### Docker Deployment

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]
```

### Production Checklist

- [ ] Set strong `SECRET_KEY` in environment
- [ ] Configure `CORS_ORIGINS` to specific domains
- [ ] Set up proper logging aggregation
- [ ] Enable HTTPS/TLS
- [ ] Implement rate limiting
- [ ] Set up monitoring and alerting
- [ ] Use production-grade database
- [ ] Configure auto-scaling
- [ ] Set up CI/CD pipeline
- [ ] Implement backup strategy

## 🎯 Future Enhancements

### Using Python Requests

```python
import requests

# Get recommendations
response = requests.get('http://localhost:5000/api/v1/recommendations/user123?limit=5')
print(response.json())

# Add interaction
interaction_data = {
    'user_id': 'user123',
    'product_id': 'P001',
    'interaction_type': 'purchase',
    'rating': 5
}
response = requests.post(
    'http://localhost:5000/api/v1/interaction',
    json=interaction_data
)
print(response.json())
```

## 🤖 Recommendation Algorithms

## 🎯 Future Enhancements

- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] User authentication and authorization (JWT)
- [ ] Advanced ML models (Matrix Factorization, Neural Collaborative Filtering)
- [ ] Real-time recommendation updates with WebSockets
- [ ] A/B testing framework
- [ ] Analytics dashboard with metrics
- [ ] Redis caching layer
- [ ] GraphQL API support
- [ ] Kubernetes deployment configs
- [ ] API documentation with Swagger/OpenAPI
- [ ] Elasticsearch for advanced product search
- [ ] Recommendation explanation features

## 📚 API Documentation

### Swagger/OpenAPI Documentation

Interactive API documentation is available at `http://localhost:5000/swagger/` when the server is running.

**Features:**
- 🔍 Browse all endpoints with detailed descriptions
- 🧪 Test API calls directly from your browser
- 📋 View request/response schemas
- 📖 See example payloads and responses
- 🔐 Test with authorization tokens

### Swagger Specification

The OpenAPI/Swagger specification is available at:
- JSON format: `http://localhost:5000/apispec.json`

You can import this into tools like Postman, Insomnia, or any OpenAPI-compatible client.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use type hints where applicable
- Write docstrings for all functions and classes
- Maintain test coverage above 80%

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ for learning and demonstration purposes.

## 📞 Support

For issues, questions, or contributions, please open an issue on the repository.

---

**Note**: This is a demonstration project. For production use, implement proper security measures, database solutions, and scalability considerations.
