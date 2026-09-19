
# Day 3 — Simple Chatbot Application

## Objective

Build a simple AI-powered chatbot application using FastAPI and the Google Gemini API.

The application demonstrates:

- FastAPI API development
- Request and response handling
- External AI API integration
- Environment variable management
- Single-agent architecture
- Multi-agent architecture
- Coordinator-based routing
- Specialized AI agents
- Separation of concerns
- Basic agent orchestration

## 1. Project Overview

This project is a placement preparation assistant that can help a student in three different ways:

1. Study — Understand technical concepts.
2. Practice — Generate practice questions.
3. Interview — Conduct technical mock interviews.

The application uses FastAPI as the backend API layer and Google Gemini as the external AI model.

## 2. Architecture

The application uses a coordinator-based multi-agent architecture.

User
 |
 v
FastAPI /chat
 |
 v
Coordinator
 /       |       
 v       v        v
Study  Practice  Interview
Agent   Agent      Agent
 \       |        /
  \      |       /
   \     |      /
      Gemini API
          |
          v
      AI Response

## 3. Components

### 3.1 FastAPI Layer

main.py exposes the /chat API endpoint and handles incoming HTTP requests.

It:

- Receives the user's message.
- Validates the request using Pydantic.
- Sends the message to the Coordinator.
- Returns the generated response as JSON.

### 3.2 Request Schema

schemas/chat.py contains the Pydantic request model.

Example:

class ChatRequest(BaseModel):
    message: str

Example request:

{
    "message": "Explain SQL JOINs"
}

This ensures that the /chat endpoint receives the expected request structure.

### 3.3 Coordinator

agents/coordinator.py is responsible for routing the user's request to the appropriate specialized agent.

The current routing logic is rule-based and uses keywords.

For example:

"Explain SQL JOINs"
        |
        v
Study Agent

"Give me SQL practice questions"
        |
        v
Practice Agent

"Take my Python mock interview"
        |
        v
Interview Agent

The Coordinator does not generate the final AI explanation itself. Its responsibility is to decide which specialized agent should handle the request.

### 3.4 Study Agent

agents/study_agent.py is responsible for helping users understand technical concepts.

Its instructions tell Gemini to:

- Explain concepts clearly.
- Use simple language.
- Assume the student is a beginner.
- Use examples when useful.
- Avoid conducting mock interviews or practice tests.

Example:

User:
Explain SQL JOINs.

Study Agent:
Provides a beginner-friendly explanation of SQL JOINs.

### 3.5 Practice Agent

agents/practice_agent.py is responsible for generating practice questions.

Its instructions tell Gemini to:

- Generate relevant practice questions.
- Adjust difficulty when possible.
- Provide solutions only when requested.
- Focus on practice rather than concept explanation or interviews.

Example:

User:
Give me 5 SQL JOIN practice questions.

Practice Agent:
Generates five SQL JOIN practice questions.

### 3.6 Interview Agent

agents/interview_agent.py is responsible for conducting technical mock interviews.

Its instructions tell Gemini to:

- Ask one question at a time.
- Wait for the candidate's answer.
- Evaluate the answer.
- Provide constructive feedback.
- Adjust questions based on the candidate's level when possible.

Example:

User:
Start a beginner Python mock interview.

Interview Agent:
Asks the first interview question.

### 3.7 Gemini API

The specialized agents use the Google Gemini API to generate AI responses.

The API key is stored in an environment variable:

GEMINI_API_KEY

The key is loaded using python-dotenv.

The .env file is intentionally excluded from Git using .gitignore.

## 4. Project Structure

Day-03-Simple-Chatbot/
|
├── .env
├── main.py
|
├── agents/
│   ├── coordinator.py
│   ├── study_agent.py
│   ├── practice_agent.py
│   └── interview_agent.py
|
├── schemas/
│   └── chat.py
|
└── README.md

## 5. API Endpoint

### POST /chat

The main chatbot endpoint is:

POST /chat

Request:

{
    "message": "I want to study SQL"
}

The request is passed to the Coordinator.

The Coordinator selects the appropriate agent.

The selected agent sends the request to Gemini.

The generated response is returned to the user.

Example response:

{
    "response": "SQL is a language used to interact with relational databases..."
}

## 6. Request Flow

The complete request flow is:

User Message
     |
     v
POST /chat
     |
     v
Pydantic Validation
     |
     v
Coordinator
     |
     v
Select Specialized Agent
     |
     v
Agent Instructions + User Message
     |
     v
Gemini API
     |
     v
Generated Response
     |
     v
FastAPI JSON Response

## 7. Single-Agent vs Multi-Agent Architecture

### Single-Agent Architecture

In a single-agent system, one AI agent handles the entire task.

User
 |
 v
Single Agent
 |
 v
Gemini
 |
 v
Response

This is simpler to implement but can become difficult to maintain when the application supports many different responsibilities.

### Multi-Agent Architecture

In this project, different responsibilities are separated into specialized agents.

User
 |
 v
Coordinator
 |
 +-- Study Agent
 |
 +-- Practice Agent
 |
 +-- Interview Agent

Each agent has its own responsibility and instructions.

This demonstrates the basic concept of agent orchestration.

## 8. Separation of Concerns

The project separates different responsibilities across different files.

Component              Responsibility

main.py                API layer
schemas/chat.py        Request validation
coordinator.py         Request routing
study_agent.py         Concept learning
practice_agent.py      Practice questions
interview_agent.py     Mock interviews

This makes the application easier to understand, test and extend.

## 9. Rule-Based Routing

The Coordinator currently uses keyword-based routing.

Study-related keywords:

- study
- learn
- understand
- explain
- concept

Practice-related keywords:

- practice
- question
- questions
- problem
- problems
- exercise

Interview-related keywords:

- interview
- mock interview
- interview me

If no relevant keyword is detected, the Coordinator asks the user to clarify their intent.

## 10. Why Rule-Based Routing?

Rule-based routing was intentionally used for this version because it is:

- Simple.
- Easy to understand.
- Easy to debug.
- Predictable.
- Easy to test.

However, it has limitations.

For example, a user may express the same intention using words that are not included in the current keyword list.

A future version could use an LLM-based router or another classification approach.

## 11. Environment Variables

The Gemini API key is stored in .env.

Example:

GEMINI_API_KEY=your_api_key_here

The .env file is not committed to Git.

This is important because API keys and other secrets should not be exposed in public repositories.

## 12. Running the Application

Navigate to the project directory:

cd ~/Desktop/AI-Engineering-Training/Day-03-Simple-Chatbot

Activate the virtual environment if required:

source ../.venv/bin/activate

Install dependencies:

pip install fastapi uvicorn google-genai python-dotenv

Start the server:

uvicorn main:app --reload

The application will run at:

http://127.0.0.1:8000

Swagger API documentation is available at:

http://127.0.0.1:8000/docs

## 13. Testing

The application was tested using FastAPI Swagger UI.

### Study Test

Request:

{
    "message": "I want to study SQL JOINs"
}

Expected routing:

Coordinator
     |
     v
Study Agent
     |
     v
Gemini

### Practice Test

Request:

{
    "message": "Give me 5 SQL JOIN practice questions"
}

Expected routing:

Coordinator
     |
     v
Practice Agent
     |
     v
Gemini

### Interview Test

Request:

{
    "message": "Take my beginner Python mock interview"
}

Expected routing:

Coordinator
     |
     v
Interview Agent
     |
     v
Gemini

### Unknown Intent Test

Request:

{
    "message": "Help me with SQL"
}

Since the intent is ambiguous, the Coordinator asks the user to clarify whether they want to study, practice or take an interview.

## 14. Key Concepts Learned

### API

An API provides an interface through which different software systems communicate.

### FastAPI

FastAPI is a Python framework used to build APIs and backend applications.

### Request and Response

The client sends a request to the API and the server returns a response.

### JSON

JSON is used to represent structured request and response data.

### External API Integration

The FastAPI application communicates with the external Gemini API to generate AI responses.

### Prompt Engineering

Agent instructions are used to control the behavior and responsibilities of each AI agent.

### Single-Agent System

One agent handles the entire task.

### Multi-Agent System

Multiple specialized agents handle different responsibilities.

### Coordinator

A Coordinator determines which specialized agent should process a request.

### Agent Orchestration

The process of coordinating multiple specialized agents to complete different parts of a workflow.

### Separation of Concerns

Different parts of the application are responsible for different tasks.

## 15. Limitations

The current implementation is intentionally simple.

Main limitations:

1. Routing is keyword-based.
2. Agents do not maintain conversation memory.
3. Interview state is not persisted between requests.
4. There is no database.
5. Authentication is not implemented.
6. Error handling for external AI API failures is minimal.
7. Each agent independently calls the Gemini API.

These limitations provide opportunities for future improvements.

## 16. Future Improvements

Possible improvements include:

- LLM-based intelligent routing.
- Conversation memory.
- Persistent interview sessions.
- Database integration.
- Authentication and authorization.
- Better error handling.
- Streaming AI responses.
- Agent-to-agent communication.
- LangChain integration.
- LangGraph-based agent workflows.
- Frontend interface using Streamlit.
- Deployment using cloud infrastructure.
- Automated testing.
- CI/CD pipeline.

## 17. Skills Demonstrated

This project demonstrates practical experience with:

- Python
- FastAPI
- REST API development
- Pydantic
- Environment variables
- External API integration
- Google Gemini API
- Prompt Engineering
- Multi-Agent Architecture
- Agent Orchestration
- Rule-Based Routing
- Backend Architecture
- Git and GitHub

## 18. Conclusion

This project demonstrates how a simple FastAPI backend can be extended into an AI-powered multi-agent application.

The main architectural idea is to separate responsibilities:

FastAPI
   |
   v
Coordinator
   |
   v
Specialized Agents
   |
   v
Gemini API
   |
   v
AI Response

The implementation provides a foundation for building more advanced Agentic AI systems using frameworks such as LangChain and LangGraph.
