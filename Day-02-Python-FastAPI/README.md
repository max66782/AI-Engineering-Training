# Day 2 — Python & FastAPI

## Objective

Learn the fundamentals of Python backend development using FastAPI and understand how to build, validate, organize, and test REST APIs.

The practical implementation focused on:

- FastAPI application setup
- HTTP methods
- API routes and endpoints
- Path parameters
- Query parameters
- Request bodies
- Pydantic schemas
- Data validation
- HTTP error handling
- Authentication basics
- Backend architecture
- Routers
- Service layer
- Separation of concerns

---

## 1. What is an API?

An API (Application Programming Interface) allows different software systems to communicate with each other.

A typical backend flow is:

```text
Frontend
   ↓
API
   ↓
Backend
   ↓
Database
   ↓
Backend
   ↓
API Response
   ↓
Frontend
```

---

## 2. What is FastAPI?

FastAPI is a modern Python framework used to build APIs.

Important features include:

- Automatic request validation
- Automatic JSON serialization
- Type-hint based development
- Automatic interactive API documentation
- High-performance API development

Interview definition:

> FastAPI is a Python framework for building high-performance REST APIs with features such as automatic validation, serialization, and interactive API documentation.

---

## 3. HTTP Methods

The main HTTP methods studied were:

| Method | Purpose              |
| ------ | -------------------- |
| GET    | Retrieve data        |
| POST   | Create/send data     |
| PUT    | Update existing data |
| DELETE | Delete data          |

Important distinction:

**GET and POST are HTTP methods, not routes.**

A route/endpoint is generally identified by the combination of:

```text
HTTP Method + Path
```

Examples:

```text
GET  /users
POST /users
GET  /users/25
```

`GET /users` and `POST /users` are different endpoints even though they use the same path.

---

## 4. Request and Response

### Request

The request is what the client sends to the server.

Example:

```text
POST /users
```

with a JSON request body.

### Response

The response is what the server sends back to the client.

Example:

```json
{
  "name": "Krishn",
  "email": "krishn@example.com",
  "age": 23
}
```

---

## 5. API Routing

A route connects an HTTP method and a path to a Python function.

Example:

```python
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
```

Conceptually:

```text
Route = WHERE
HTTP Method = WHAT
Function = HOW
```

---

## 6. Path Parameters

Path parameters are used to identify a specific resource.

Example:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Request:

```text
GET /users/25
```

Here:

```text
user_id = 25
```

The value `25` is a path parameter.

### Why use a path parameter?

It is useful when identifying a specific resource.

```text
/users/25
```

means:

> Get user 25.

---

## 7. Query Parameters

Query parameters are passed after `?` in the URL.

Example:

```python
@app.get("/products")
def get_products(category: str):
    return {"category": category}
```

Request:

```text
GET /products?category=shoes
```

Here:

```text
category = parameter name
shoes    = parameter value
```

Query parameters are commonly used for filtering, sorting, searching, and optional configuration.

### Path vs Query Parameter

```text
/users/25
```

→ identifies a specific user.

```text
/users?age=25
```

→ filters users based on age.

Easy way to remember:

> Path parameter = which resource?

> Query parameter = how/filter the resource?

---

## 8. Request Body

A request body is used to send structured data to the server, commonly with POST requests.

Example:

```json
{
  "name": "Krishn",
  "email": "krishn@example.com",
  "age": 23
}
```

---

## 9. Pydantic Schemas

Pydantic models define the expected structure and types of API data.

Example:

```python
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    email: str
    age: int = Field(ge=18)
```

This defines:

```text
name  → string
email → string
age   → integer and >= 18
```

The schema was placed in:

```text
schemas/user.py
```

This keeps request/response validation separate from API routing.

---

## 10. Automatic Validation

FastAPI and Pydantic automatically validate incoming request data.

For example:

```python
age: int
```

expects an integer.

This request is invalid:

```json
{
  "name": "Krishn",
  "email": "krishn@example.com",
  "age": "twenty three"
}
```

FastAPI returns a validation error instead of passing invalid data to the route function.

We also implemented:

```python
age: int = Field(ge=18)
```

Therefore:

```text
23 → valid
18 → valid
17 → invalid
"abc" → invalid
```

---

## 11. HTTPException and Error Handling

FastAPI provides `HTTPException` for controlled API errors.

Example:

```python
if user_id not in [1, 2, 3]:
    raise HTTPException(
        status_code=404,
        detail="user not found"
    )
```

Request:

```text
GET /users/999
```

produces:

```json
{
  "detail": "user not found"
}
```

with HTTP status:

```text
404 Not Found
```

---

## 12. Authentication Basics

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to do?

Typical authentication flow:

```text
User
 ↓
Login credentials
 ↓
Authentication
 ↓
JWT Token
 ↓
Future API request
 ↓
Server verifies token
 ↓
Access granted/rejected
```

A JWT can be sent using:

```text
Authorization: Bearer <token>
```

Authentication and authorization are separate concepts.

---

## 13. Backend Architecture

Instead of putting the entire backend inside one file, responsibilities can be separated into different modules.

Our project structure became:

```text
Day-02-Python-FastAPI/
│
├── main.py
│
├── routes/
│   ├── users.py
│   └── products.py
│
├── schemas/
│   └── user.py
│
├── services/
│   └── user_service.py
│
└── models/
```

### Responsibilities

| Component     | Responsibility                            |
| ------------- | ----------------------------------------- |
| `main.py`   | Application setup                         |
| `routes/`   | API endpoints                             |
| `schemas/`  | Request/response structure and validation |
| `services/` | Business/application logic                |
| `models/`   | Database models                           |

---

## 14. Routers

Instead of defining every endpoint directly inside `main.py`, FastAPI's `APIRouter` can organize related endpoints.

Example:

```python
from fastapi import APIRouter

router = APIRouter()
```

User endpoints were placed in:

```text
routes/users.py
```

Product endpoints were placed in:

```text
routes/products.py
```

The routers are then connected to the main application:

```python
app.include_router(users_router)
app.include_router(products_router)
```

This improves organization and scalability.

---

## 15. Service Layer

The service layer contains business/application logic.

Our user service:

```text
services/user_service.py
```

contains the `create_user()` function.

The route calls the service instead of containing all the business logic itself.

```text
POST /users
     ↓
routes/users.py
     ↓
create_user_service()
     ↓
services/user_service.py
     ↓
Business Logic
     ↓
Response
```

This separation makes the code easier to maintain and extend.

---

## 16. Schema vs Model

### Schema

Defines the structure and validation of data entering or leaving the API.

Example:

```python
class User(BaseModel):
    name: str
    email: str
    age: int
```

### Model

Represents how data is structured/stored in the database.

Conceptually:

```text
Client
  ↓
Schema
  ↓
Route
  ↓
Service
  ↓
Database Model
  ↓
Database
```

The project created the `models/` directory for future database integration.

---

## 17. Practical API Endpoints Implemented

### GET `/`

Returns a basic FastAPI response.

Example:

```json
{
  "message": "Hello, FastAPI!"
}
```

### GET `/users`

Returns a list of users.

Example:

```json
{
  "users": [
    "Rahul",
    "Ankit",
    "Priya"
  ]
}
```

### GET `/users/{user_id}`

Uses a path parameter.

Example:

```text
GET /users/2
```

Response:

```json
{
  "user_id": 2
}
```

### GET `/products?category=shoes`

Uses a query parameter.

Response:

```json
{
  "category": "shoes"
}
```

### POST `/users`

Accepts a validated request body.

Example:

```json
{
  "name": "Krishn",
  "email": "krishn@example.com",
  "age": 23
}
```

---

## 18. Interactive API Documentation

FastAPI automatically generated Swagger UI.

Documentation was accessed through:

```text
http://127.0.0.1:8000/docs
```

Swagger was used to:

- View available endpoints
- Execute GET requests
- Execute POST requests
- Provide request bodies
- Test path parameters
- Test query parameters
- Observe validation errors
- Observe HTTP errors

---

## 19. Development Environment

Python virtual environment:

```text
.venv/
```

Packages installed:

```text
fastapi
uvicorn
```

The application was started using:

```bash
uvicorn main:app --reload
```

The `--reload` option automatically reloads the development server when code changes.

---

## 20. Testing Performed

The following cases were tested successfully:

### Valid path parameter

```text
GET /users/2
```

→ Successful response.

### Invalid path parameter type

```text
GET /users/abc
```

→ Validation error.

### Valid query parameter

```text
GET /products?category=shoes
```

→ Successful response.

### Valid POST request

```json
{
  "name": "Krishn",
  "email": "krishn@example.com",
  "age": 23
}
```

→ Successful response.

### Invalid POST data

```json
{
  "name": "Krishn",
  "email": "krishn@example.com",
  "age": "twenty three"
}
```

→ Pydantic validation error.

### Age constraint

```json
{
  "name": "Krishn",
  "email": "krishn@example.com",
  "age": 17
}
```

→ Validation error because `age >= 18` is required.

### Non-existent user

```text
GET /users/999
```

→ `404 Not Found`.

---

## 21. Key Learnings

By completing Day 2, I learned how to:

- Build APIs using FastAPI
- Understand HTTP methods
- Create API routes/endpoints
- Work with path parameters
- Work with query parameters
- Handle JSON request bodies
- Create Pydantic schemas
- Implement automatic validation
- Add custom validation constraints
- Handle API errors using `HTTPException`
- Understand authentication and authorization
- Organize FastAPI applications using routers
- Separate schemas from routes
- Separate business logic into services
- Understand the role of database models
- Test APIs using Swagger UI
- Run FastAPI using Uvicorn

---

## 22. Interview-Ready Explanations

### What is FastAPI?

> FastAPI is a modern Python framework for building high-performance REST APIs with automatic validation, serialization, and interactive API documentation.

### What is a path parameter?

> A path parameter is a value included directly in the URL path and is generally used to identify a specific resource.

### What is a query parameter?

> A query parameter is a parameter provided after `?` in the URL and is commonly used for filtering or customizing API results.

### What is Pydantic used for?

> Pydantic is used to define data schemas and validate incoming and outgoing data based on Python type annotations and validation rules.

### Why use a service layer?

> The service layer contains business logic and keeps it separate from HTTP-specific route handling, improving maintainability and scalability.

### Authentication vs Authorization

> Authentication verifies a user's identity, while authorization determines what an authenticated user is allowed to access or perform.

### Why separate routes and services?

> Routes handle HTTP communication, while services handle business logic. Separating them reduces coupling and makes the application easier to maintain and scale.

---

## Status

**Day 2 — Python & FastAPI: COMPLETE ✅**

Next stage:

**Day 3 — Simple Chatbot Application**

The Day 3 project will build on the FastAPI concepts learned here and introduce API integration and AI/LLM-based application workflows.
