# Day 10 — n8n Agentic AI

## Objective

Build a practical AI Interview Assistant using n8n, Google Gemini, AI Agent, custom tools, and memory.

## Workflow

Chat Trigger
↓
AI Agent
↓
Google Gemini Chat Model

AI Agent also connects to:
- Code Tool
- Simple Memory

## Technologies

- n8n Cloud
- Google Gemini
- n8n AI Agent
- Code Tool
- Simple Memory
- Chat Trigger

## What I Learned

### n8n

n8n is a workflow automation platform where applications and AI components can be connected through nodes.

### Workflow

A workflow is a sequence of connected nodes that process data and perform actions.

### Chat Trigger

The Chat Trigger starts the workflow when a user sends a chat message.

### AI Agent

The AI Agent receives the user's request, uses the configured language model, and can decide when to use available tools.

### Chat Model

Google Gemini acts as the language model that generates the AI responses.

### Tools

The Code Tool gives the AI Agent an external capability that it can invoke when required.

The custom tool was configured to convert text to uppercase.

### Memory

Simple Memory allows the AI Agent to maintain conversation context using the chat session ID.

## System Message

The agent was configured as an AI Interview Preparation Assistant focused on:

- Python
- SQL
- Data Structures & Algorithms
- Backend Development
- AI/ML
- Data Engineering

## Testing

### Test 1 — Basic Chat

Input:

Hello

Result:

The AI Agent generated a response successfully.

### Test 2 — Tool Invocation

Input:

Convert this to uppercase: data engineering interview

Result:

DATA ENGINEERING INTERVIEW

The execution logs confirmed that the AI Agent invoked the Code Tool.

### Test 3 — Interview Assistant

Input:

Ask me one Python interview question.

Result:

The agent generated a relevant Python interview question.

### Test 4 — Tool + Interview Question

Input:

Convert "python interview preparation" to uppercase, then ask me one SQL interview question.

Result:

PYTHON INTERVIEW PREPARATION

The agent then generated a SQL interview question.

### Test 5 — Memory

First message:

My name is Krishn.

Second message:

What is my name?

Result:

The agent correctly remembered the name Krishn.

## Final Architecture

Chat Trigger
        ↓
     AI Agent
     ↙      ↘
Gemini      Tools
             ↓
         Code Tool

        ↑
   Simple Memory

## Verification

- Chat Trigger tested successfully
- Gemini Chat Model tested successfully
- AI Agent tested successfully
- Code Tool invocation verified through execution logs
- Simple Memory tested successfully
- End-to-end interview assistant tested successfully