
# Day 4 — Frontend UI with Streamlit

## Objective

Build a frontend interface for the Day 3 AI placement preparation chatbot using Streamlit.

The frontend communicates with the existing FastAPI backend through a REST API instead of containing the chatbot or Gemini logic itself.

The goal of this day was to understand how an AI backend can be connected to a user-facing frontend.

---

## Project Overview

This project provides a chatbot interface for a placement preparation assistant.

The chatbot supports three types of requests:

- **Study** — Explain technical concepts
- **Practice** — Generate practice questions
- **Interview** — Conduct mock technical interviews

The Streamlit application acts only as the frontend. The existing FastAPI backend from Day 3 continues to handle routing, agents, and Gemini API communication.

---

## Final Architecture

```text
User
 ↓
Streamlit Frontend
 ↓ HTTP POST /chat
FastAPI Backend
 ↓
Coordinator
 ↓
Study / Practice / Interview Agent
 ↓
Gemini API
 ↓
FastAPI Response
 ↓
Streamlit UI
```

### Component Responsibilities

| Component       | Responsibility                  |
| --------------- | ------------------------------- |
| Streamlit       | User interface                  |
| Requests        | HTTP communication with backend |
| FastAPI         | Backend API                     |
| Coordinator     | Routes the request              |
| Study Agent     | Explains concepts               |
| Practice Agent  | Generates practice questions    |
| Interview Agent | Conducts mock interviews        |
| Gemini          | Generates AI responses          |

---

## Project Structure

```text
Day-04-Frontend-UI/
├── app.py
└── README.md
```

The FastAPI backend remains in the Day 3 project:

```text
Day-03-Simple-Chatbot/
├── agents/
│   ├── coordinator.py
│   ├── interview_agent.py
│   ├── practice_agent.py
│   └── study_agent.py
├── schemas/
│   └── chat.py
├── main.py
└── README.md
```

---

# Technologies Used

- Python
- Streamlit
- Requests
- FastAPI
- Pydantic
- Google Gemini API
- Python virtual environment

---

# Streamlit

## What is Streamlit?

Streamlit is a Python framework for quickly building interactive web applications.

It allows Python developers to create user interfaces without writing traditional frontend code such as HTML, CSS, or JavaScript.

In this project, Streamlit is used to create the chatbot frontend.

---

# Basic Streamlit UI

The application starts with:

```python
import streamlit as st
import requests

st.title("Placement Preparation Assistant")

st.caption("AI-powered placement preparation assistant")
```

`st.title()` displays the main application heading.

`st.caption()` displays secondary descriptive text.

---

# Chat Input

The application uses Streamlit's built-in chat input:

```python
user_message = st.chat_input("What do you want to learn?")
```

This provides a chatbot-style input field.

When the user submits a message, Streamlit reruns the application and provides the submitted message through `user_message`.

---

# Chat Messages

Streamlit provides `st.chat_message()` for displaying messages in a chatbot interface.

```python
with st.chat_message("user"):
    st.write(user_message)
```

Assistant responses are displayed using:

```python
with st.chat_message("assistant"):
    st.write(assistant_message)
```

This creates separate user and assistant chat bubbles.

---

# Session State

Streamlit reruns the Python script when users interact with the application.

Therefore, normal Python variables do not reliably preserve conversation history between reruns.

To maintain chat history, the application uses:

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

Messages are stored as dictionaries:

```python
{
    "role": "user",
    "content": "Explain SQL JOINs"
}
```

or:

```python
{
    "role": "assistant",
    "content": "An INNER JOIN returns..."
}
```

The conversation can then be displayed using:

```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
```

### Important Limitation

This chat history exists only in the Streamlit session.

It is not persistent storage.

If the application/server session is restarted, the conversation history is lost.

A production application could use a database, cache, or dedicated conversation-storage system for persistent history.

---

# Clear Chat

The application provides a Clear Chat button:

```python
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
```

This:

1. Clears the stored conversation.
2. Reruns the Streamlit application.
3. Displays an empty chat.

---

# REST API Integration

The Streamlit frontend does not directly communicate with Gemini.

Instead, it communicates with the existing FastAPI backend.

The frontend sends:

```python
response = requests.post(
    "http://127.0.0.1:8000/chat",
    json={"message": user_message}
)
```

This creates an HTTP POST request to:

```text
http://127.0.0.1:8000/chat
```

The request body is JSON:

```json
{
  "message": "Explain SQL JOINs"
}
```

---

# Why Use the FastAPI Backend?

The frontend should not contain the Gemini API key or AI business logic.

The architecture is therefore:

```text
Streamlit
   ↓
FastAPI
   ↓
AI Logic
   ↓
Gemini
```

Instead of:

```text
Streamlit
   ↓
Gemini API
```

This separation provides better:

- Security
- Maintainability
- Separation of concerns
- Scalability
- Backend control
- API management

---

# JSON Response

FastAPI returns a response in the following structure:

```json
{
  "response": "AI generated response..."
}
```

The Streamlit frontend extracts the response using:

```python
assistant_message = response.json()["response"]
```

The response is then displayed in the assistant chat bubble.

---

# Complete Request Flow

When a user enters:

```text
Explain INNER JOIN
```

the following happens:

```text
1. User enters message
        ↓
2. Streamlit receives the message
        ↓
3. Streamlit sends POST /chat
        ↓
4. FastAPI receives JSON request
        ↓
5. Coordinator analyzes the request
        ↓
6. Coordinator selects Study Agent
        ↓
7. Study Agent sends prompt to Gemini
        ↓
8. Gemini generates response
        ↓
9. Study Agent returns response
        ↓
10. FastAPI returns JSON
        ↓
11. Streamlit receives JSON
        ↓
12. Streamlit displays assistant response
```

---

# Error Handling

The frontend uses `try/except` to handle backend connection problems:

```python
try:
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": user_message}
    )

    response.raise_for_status()

except requests.exceptions.RequestException as e:
    st.error(f"Could not connect to the backend: {e}")
```

`raise_for_status()` raises an exception when the HTTP response contains an error status.

For example:

```text
404 Not Found
422 Unprocessable Entity
500 Internal Server Error
```

This prevents the frontend from failing silently and gives the user a readable error message.

---

# Empty Message Protection

The application checks:

```python
if user_message and user_message.strip():
```

This prevents empty or whitespace-only messages from being sent to the backend.

---

# Why Streamlit Instead of React?

For this training project, Streamlit was chosen because the goal is to quickly build and understand an AI application frontend using Python.

### Streamlit

Advantages:

- Very fast development
- Python-based
- Minimal frontend code
- Built-in chatbot components
- Excellent for prototypes and internal AI tools

### React

React is more appropriate when building highly customized production web interfaces.

It provides greater control over:

- UI design
- Components
- Client-side state
- Routing
- Browser interactions
- Complex frontend architecture

The choice depends on the project requirements.

For this training project, Streamlit allows us to focus on understanding the AI application architecture and API integration.

---

# Frontend vs Backend

## Frontend

The frontend is responsible for:

- Displaying the UI
- Accepting user input
- Displaying chat messages
- Sending requests to the backend
- Displaying responses

In this project:

```text
Streamlit
```

is the frontend.

## Backend

The backend is responsible for:

- API endpoints
- Request validation
- Routing
- AI agent selection
- Gemini API communication
- Business logic

In this project:

```text
FastAPI
```

is the backend.

---

# Why Keep Gemini on the Backend?

The Gemini API key is a secret and should not be exposed to the browser/frontend.

Therefore:

```text
Correct:

Browser
   ↓
Streamlit
   ↓
FastAPI
   ↓
Gemini API
```

The Gemini API key remains inside the backend environment.

The frontend only communicates with our API.

---

# Integration With Day 3

Day 4 intentionally reuses the Day 3 backend.

We did not duplicate:

- Gemini logic
- Agent logic
- Coordinator logic
- API key handling

The existing backend remains responsible for AI functionality.

Day 4 adds a frontend layer on top of it.

This demonstrates separation of concerns.

---

# Testing

The application was tested through the Streamlit browser.

## Study Agent Test

Input:

```text
Explain SQL JOINs
```

Expected behavior:

```text
Streamlit
→ FastAPI
→ Coordinator
→ Study Agent
→ Gemini
```

Result:

Successfully returned an explanation of SQL JOINs.

---

## Practice Agent Test

Input:

```text
Give me 3 SQL JOIN practice questions
```

Expected behavior:

```text
Streamlit
→ FastAPI
→ Coordinator
→ Practice Agent
→ Gemini
```

Result:

Successfully generated SQL practice questions.

---

## Interview Agent Test

Input:

```text
Take my Python mock interview
```

Expected behavior:

```text
Streamlit
→ FastAPI
→ Coordinator
→ Interview Agent
→ Gemini
```

Result:

Successfully started the mock interview.

---

## Error Handling Test

The FastAPI server was temporarily stopped while making a request from Streamlit.

The frontend displayed a readable connection error instead of crashing.

The FastAPI server was then restarted and the application was tested again successfully.

---

## Chat History Test

Multiple messages were sent sequentially.

The application successfully preserved:

```text
User message
Assistant response
User message
Assistant response
```

using:

```python
st.session_state.messages
```

---

## Clear Chat Test

The Clear Chat button was tested successfully.

The stored messages were removed and the UI was rerendered without the previous conversation.

---

# Running the Application

## 1. Activate the virtual environment

From the repository root:

```bash
source .venv/bin/activate
```

---

## 2. Start the FastAPI backend

Open a terminal and run:

```bash
cd Day-03-Simple-Chatbot
uvicorn main:app --reload
```

The backend runs at:

```text
http://127.0.0.1:8000
```

---

## 3. Start the Streamlit frontend

Open another terminal and run:

```bash
cd Day-04-Frontend-UI
streamlit run app.py
```

Streamlit will provide a local URL in the terminal.

Open that URL in the browser.

---

# Important Environment Variables

The Gemini API key belongs to the backend.

It is stored in the Day 3 `.env` file:

```text
GEMINI_API_KEY=...
```

The `.env` file is excluded from Git using `.gitignore`.

The Streamlit frontend does not contain the Gemini API key.

---

# Key Concepts Learned

## Streamlit

- Streamlit applications
- `st.title()`
- `st.caption()`
- `st.chat_input()`
- `st.chat_message()`
- `st.button()`
- `st.session_state`
- `st.rerun()`

## API Integration

- HTTP requests
- HTTP POST
- REST API
- JSON request body
- JSON response
- HTTP status codes
- Error handling

## Software Architecture

- Frontend/backend separation
- Separation of concerns
- API abstraction
- Reusing existing backend services
- Keeping secrets on the backend

## AI Application Architecture

- LLM integration
- Multi-agent architecture
- Coordinator-based routing
- Specialized agents
- Frontend-to-AI backend communication

---

# Important Interview Questions

### What is Streamlit?

Streamlit is a Python framework for creating interactive web applications quickly, particularly useful for data and AI applications.

### How does Streamlit communicate with FastAPI?

The Streamlit application sends an HTTP request using the `requests` library to the FastAPI endpoint.

### What is REST?

REST is an architectural style for designing networked applications around resources and standard HTTP methods such as GET, POST, PUT, and DELETE.

### What is JSON?

JSON is a lightweight data-interchange format commonly used for communication between frontend and backend systems.

### What happens when the user clicks Send?

The frontend sends the user's message as JSON to the FastAPI `/chat` endpoint. FastAPI passes it to the Coordinator, which selects the appropriate agent. The agent communicates with Gemini and returns the generated response to FastAPI, which sends it back to Streamlit.

### Why should API keys stay on the backend?

API keys are sensitive credentials. Exposing them in frontend code can allow unauthorized users to access the API and potentially incur costs or abuse the service.

### Why use `st.session_state`?

Streamlit reruns the application when users interact with the UI. `st.session_state` allows information such as chat history to persist between those reruns.

### Why use a separate FastAPI backend?

It keeps the frontend separate from AI and business logic and provides a reusable API layer that other clients could also consume.

---

# Limitations

This project is intentionally simple and designed for learning.

Current limitations include:

- Rule-based Coordinator routing
- Chat history exists only within the Streamlit session
- No user authentication
- No database persistence
- No streaming token responses
- No production deployment
- No advanced observability
- No automated evaluation system
- No sophisticated agent planning
- No persistent long-term memory

These are potential areas for future improvements.

---

# Future Improvements

Possible future improvements include:

- Persistent conversation storage
- User authentication
- Streaming AI responses
- Better UI customization
- Advanced intent classification
- Retrieval-Augmented Generation (RAG)
- Tool calling
- Agent workflows
- LangChain integration
- LangGraph workflows
- Automated evaluation
- Logging and monitoring
- Dockerization
- CI/CD
- Cloud deployment

---

# Day 4 Learning Outcome

By completing Day 4, the project evolved from a backend-only AI chatbot into a complete basic AI application:

```text
                Placement Preparation Assistant
                            │
                     Streamlit UI
                            │
                         REST API
                            │
                         FastAPI
                            │
                       Coordinator
                     /      |       \
                    /       |        \
               Study    Practice   Interview
                 \         |          /
                  \        |         /
                       Gemini
```

The main learning was that an AI application is not just an LLM prompt.

A useful AI system combines:

```text
Frontend
+
Backend
+
APIs
+
AI Models
+
Application Logic
+
State Management
+
Error Handling
```

---

# Skills Demonstrated

- Python
- Streamlit
- FastAPI
- REST API integration
- HTTP requests
- JSON
- Session state
- Chat UI development
- Error handling
- Multi-agent architecture
- Gemini API integration
- Frontend/backend separation
- Git/GitHub project documentation

---

# Conclusion

Day 4 introduced the frontend layer for the AI Engineering training project.

The existing Day 3 FastAPI multi-agent chatbot was successfully connected to a Streamlit frontend.

The final application allows users to interact with Study, Practice, and Interview agents through a browser-based chatbot interface.

The project demonstrates the basic architecture used to build an AI-powered application where the frontend, backend, AI orchestration, and foundation model remain separated into distinct responsibilities.
