# Swagger/OpenAPI Documentation Guide

## Overview

This project uses **Flasgger** to provide interactive API documentation via Swagger UI, following the OpenAPI 2.0 specification.

## Accessing Swagger UI

Once the server is running, visit:
```
http://localhost:5000/swagger/
```

## Swagger Features

### 1. **Interactive Testing**
- Click on any endpoint to expand it
- Click "Try it out" button
- Fill in parameters
- Click "Execute" to test the API
- View the response in real-time

### 2. **API Specification**
The OpenAPI specification is available at:
```
http://localhost:5000/apispec.json
```

You can import this into:
- Postman
- Insomnia
- Swagger Editor
- Any OpenAPI-compatible tool

## Endpoint Documentation Structure

Each endpoint includes:

### Parameters
- **Path Parameters**: Required values in the URL
- **Query Parameters**: Optional filters and limits
- **Body Parameters**: Request payload for POST/PUT

### Responses
- **200/201**: Success responses with schema
- **400**: Bad request/validation errors
- **500**: Internal server errors

### Examples
- Request examples for each parameter
- Response examples showing data structure

## Using Swagger for Development

### Testing Endpoints

1. **GET Endpoints**:
   ```
   GET /api/v1/trending?limit=5
   ```
   - Enter query parameters in the UI
   - Click Execute
   - View JSON response

2. **POST Endpoints**:
   ```
   POST /api/v1/interaction
   ```
   - Fill in the request body JSON
   - Click Execute
   - View the created resource

### Example Workflow

**Scenario: Add interaction and get recommendations**

1. Open Swagger UI at `/swagger/`

2. Test health check:
   - Expand `GET /api/v1/health`
   - Click "Try it out"
   - Click "Execute"
   - Verify 200 OK response

3. Add user interaction:
   - Expand `POST /api/v1/interaction`
   - Click "Try it out"
   - Enter JSON:
     ```json
     {
       "user_id": "test_user_001",
       "product_id": "P001",
       "interaction_type": "purchase",
       "rating": 5.0
     }
     ```
   - Click "Execute"
   - Verify 201 Created

4. Get recommendations:
   - Expand `GET /api/v1/recommendations/{user_id}`
   - Enter `test_user_001` in user_id field
   - Set limit to `10`
   - Click "Execute"
   - View personalized recommendations

## Customizing Swagger

### Configuration
Located in `config/swagger_config.py`:

```python
swagger_config = {
    "specs_route": "/swagger/",  # Change UI path
    "title": "Your API Title",
    "version": "1.0.0",
    # ... more options
}
```

### Template
The `swagger_template` defines:
- API metadata (title, description, version)
- Base path and schemes
- Tags for organizing endpoints
- Security definitions (future JWT implementation)

### Adding New Endpoints

When creating new endpoints, follow this docstring format:

```python
@api_bp.route('/new-endpoint', methods=['GET'])
def new_endpoint():
    """
    Brief description
    ---
    tags:
      - Category
    parameters:
      - name: param_name
        in: query
        type: string
        required: true
        description: Parameter description
        example: "example_value"
    responses:
      200:
        description: Success response
        schema:
          type: object
          properties:
            field_name:
              type: string
              example: "value"
    """
    # Implementation
```

## Swagger Tags

Endpoints are organized by tags:

- **Health**: System health checks
- **Recommendations**: Personalized recommendations
- **Products**: Product search and discovery
- **Interactions**: User behavior tracking

## Schema Definitions

### Common Schemas

**Product Object**:
```json
{
  "product_id": "P001",
  "name": "Product Name",
  "category": "Category",
  "price": 99.99,
  "rating": 4.5
}
```

**Error Response**:
```json
{
  "error": "Error message"
}
```

## Best Practices

1. **Always provide examples** in parameters and responses
2. **Document all status codes** that can be returned
3. **Use descriptive parameter names** and descriptions
4. **Group related endpoints** with appropriate tags
5. **Keep schemas consistent** across endpoints

## Troubleshooting

### Swagger UI Not Loading
- Check that Flask server is running
- Verify flasgger is installed: `pip install flasgger`
- Check browser console for errors

### Endpoints Not Appearing
- Verify docstring format (must use `---` separator)
- Check indentation in YAML docstrings
- Restart Flask server after changes

### Test Requests Failing
- Check CORS settings in production
- Verify request payload matches schema
- Check server logs for detailed errors

## Production Considerations

### Security
In production, consider:
- Disabling Swagger UI: `swagger_ui: False`
- Restricting access to documentation
- Adding authentication to Swagger routes

### Performance
- Swagger UI is served as static files
- Minimal performance impact
- Can be disabled without affecting API

## Additional Resources

- [Flasgger Documentation](https://github.com/flasgger/flasgger)
- [OpenAPI 2.0 Specification](https://swagger.io/specification/v2/)
- [Swagger Editor](https://editor.swagger.io/)

## API Client Generation

You can generate API clients from the OpenAPI spec:

```bash
# Install OpenAPI Generator
npm install -g @openapitools/openapi-generator-cli

# Generate Python client
openapi-generator-cli generate \
  -i http://localhost:5000/apispec.json \
  -g python \
  -o ./client

# Generate JavaScript client
openapi-generator-cli generate \
  -i http://localhost:5000/apispec.json \
  -g javascript \
  -o ./client-js
```

This creates fully typed API clients in your preferred language!
