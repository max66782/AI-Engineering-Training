# Day 5 — API Integration

## Objective

Learn how REST APIs work and practice API integration using Python, FastAPI, and third-party APIs.

## Concepts Covered

- REST APIs
- HTTP methods
- HTTP requests
- HTTP headers
- JSON
- Authentication
- API keys
- HTTP status codes
- Third-party API integration
- Error handling
- Request timeouts

## 1. REST APIs

A REST API allows different applications and systems to communicate with each other over HTTP.

Common HTTP methods:

- GET — retrieve data
- POST — send or create data
- PUT — update data
- PATCH — partially update data
- DELETE — remove data

An HTTP request can contain:

- Method
- URL
- Headers
- Body

Example:

    POST /chat
    Content-Type: application/json

Request body:

    {
      "message": "Explain SQL JOINs"
    }

## 2. JSON

JSON (JavaScript Object Notation) is a lightweight, language-independent data interchange format commonly used by REST APIs.

Example:

    {
      "message": "Hello"
    }

Here:

- `message` is the key
- `"Hello"` is the value

JSON is widely used because applications written in different programming languages can exchange data using the same format.

## 3. Authentication

Authentication verifies the identity of a client or user.

In this project, a simple API key is used to protect the `/protected` endpoint.

Expected API key:

    my-secret-key

### Successful Authentication

Correct API key:

    api-key: my-secret-key

Response:

    {
      "message": "You accessed a protected endpoint"
    }

Status code:

    200 OK

### Failed Authentication

Incorrect API key:

    api-key: wrong-key

Response:

    {
      "detail": "Invalid API key"
    }

Status code:

    401 Unauthorized

## 4. FastAPI Protected Endpoint

The protected endpoint uses FastAPI's `Header` functionality to read the API key from the request headers.

    @app.get("/protected")
    def protected(api_key: str = Header()):
        if api_key != "my-secret-key":
            raise HTTPException(status_code=401, detail="Invalid API key")

        return {
            "message": "You accessed a protected endpoint"
        }

## 5. HTTP Status Codes

| Status Code | Meaning |
|-------------|---------|
| 200 | Request successful |
| 401 | Authentication failed |
| 403 | Authenticated but not authorized |
| 404 | Resource not found |
| 422 | Request validation failed |
| 500 | Internal server error |

## 6. Third-Party API Integration

A third-party API is an API provided by another service that our application can consume.

Instead of implementing every functionality ourselves, we can use existing APIs to obtain data or services.

Examples:

- Weather APIs
- GitHub APIs
- Payment APIs
- Maps APIs
- AI APIs

For this exercise, the GitHub REST API was used.

## 7. Calling GitHub API Using Python

The `requests` library was used to send an HTTP GET request.

    import requests

    response = requests.get(
        "https://api.github.com",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print("Status:", response.status_code)
    print("Content-Type:", response.headers["Content-Type"])
    print("Current User API:", data["current_user_url"])

Output:

    Status: 200
    Content-Type: application/json; charset=utf-8
    Current User API: https://api.github.com/user

This demonstrated how to:

1. Send an HTTP request
2. Receive an HTTP response
3. Check the status code
4. Inspect response headers
5. Parse JSON
6. Extract a specific value

## 8. Working With JSON Responses

The GitHub API response was converted into a Python dictionary using:

    data = response.json()

A specific value was then extracted using its key:

    data["current_user_url"]

Output:

    https://api.github.com/user

## 9. HTTP Headers

HTTP headers contain metadata about a request or response.

For example:

    print(response.headers["Content-Type"])

Output:

    application/json; charset=utf-8

This indicates that the server returned JSON data using UTF-8 character encoding.

Headers can also be used for authentication, content type, caching information, and other metadata.

## 10. Request Timeout

A timeout was added to prevent the application from waiting indefinitely for an API response.

    response = requests.get(
        "https://api.github.com",
        timeout=10
    )

Here, `timeout=10` means the request will wait for a limited amount of time before timing out.

## 11. Error Handling With raise_for_status()

The following method was used:

    response.raise_for_status()

It checks the HTTP status code and raises an exception when the request was unsuccessful.

An intentionally invalid GitHub endpoint was tested:

    https://api.github.com/this-does-not-exist

The API returned:

    404 Client Error: Not Found

Python raised:

    requests.exceptions.HTTPError

This prevents the program from silently continuing after an unsuccessful API request.

## 12. API Integration Flow

The overall REST API integration flow is:

    Client
       |
       v
    HTTP Request
       |
       v
    API Server
       |
       v
    HTTP Response
       |
       +---- Status Code
       |
       +---- Headers
       |
       +---- JSON Body
       |
       v
    Application Processes Response

For a third-party API:

    Our Application
          |
          v
    requests.get()
          |
          v
    GitHub REST API
          |
          v
    HTTP Response
          |
          v
    JSON Data
          |
          v
    Our Application

## 13. Project Files

### main.py

FastAPI application demonstrating:

- Basic API endpoint
- Protected API endpoint
- API key authentication
- HTTP headers
- HTTP 401 error handling

### github_api_test.py

Python script demonstrating:

- Third-party REST API integration
- HTTP GET request
- Status code handling
- Response headers
- JSON parsing
- Extracting JSON data
- Request timeout
- HTTP error handling

## 14. Testing Performed

### Protected Endpoint — Correct API Key

Request:

    api-key: my-secret-key

Result:

    200 OK

Response:

    {
      "message": "You accessed a protected endpoint"
    }

### Protected Endpoint — Incorrect API Key

Request:

    api-key: wrong-key

Result:

    401 Unauthorized

Response:

    {
      "detail": "Invalid API key"
    }

### GitHub API — Successful Request

Result:

    200 OK

### GitHub API — Invalid Endpoint

Result:

    404 Not Found

`raise_for_status()` correctly raised:

    requests.exceptions.HTTPError

## 15. Key Learnings

- REST APIs allow different applications to communicate over HTTP.
- HTTP methods define the type of operation being performed.
- JSON is a common language-independent data exchange format.
- HTTP headers carry metadata and can contain authentication information.
- API keys can be used to protect endpoints.
- Status codes communicate the result of an HTTP request.
- Third-party APIs allow applications to consume existing data and services.
- `requests` can be used to call REST APIs from Python.
- `response.json()` converts a JSON response into a Python object.
- `response.raise_for_status()` helps detect unsuccessful HTTP requests.
- Timeouts prevent requests from waiting indefinitely.

## Conclusion

Day 5 focused on understanding and practicing API integration.

The implementation included a FastAPI endpoint protected by API-key authentication and a Python script that consumes the GitHub REST API.

The exercises covered the complete basic API workflow:

    Request
       |
       v
    Authentication
       |
       v
    API
       |
       v
    Status Code
       |
       v
    Headers
       |
       v
    JSON Response
       |
       v
    Data Processing
       |
       v
    Error Handling

This provides the foundation required for integrating external services into real-world AI and backend applications.