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
