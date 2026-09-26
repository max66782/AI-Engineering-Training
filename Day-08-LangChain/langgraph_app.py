import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")

print("API key loaded:", True)

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=api_key,
)


class InterviewState(TypedDict):
    topic: str
    explanation: str
    questions: str


def generate_explanation(state: InterviewState):
    topic = state["topic"]

    response = model.invoke(
        f"Explain {topic} in simple terms for a beginner."
    )

    return {
        "explanation": response.content
    }


def generate_questions(state: InterviewState):
    topic = state["topic"]
    explanation = state["explanation"]

    response = model.invoke(
        f"""
        Based on the following topic and explanation,
        generate 3 technical interview questions.

        Topic:
        {topic}

        Explanation:
        {explanation}
        """
    )

    return {
        "questions": response.content
    }


graph = StateGraph(InterviewState)

graph.add_node("generate_explanation", generate_explanation)
graph.add_node("generate_questions", generate_questions)

graph.add_edge(START, "generate_explanation")
graph.add_edge("generate_explanation", "generate_questions")
graph.add_edge("generate_questions", END)

app = graph.compile()


topic = input("Enter a topic for interview preparation: ")

result = app.invoke({
    "topic": topic,
    "explanation": "",
    "questions": "",
})

print("\n==============================")
print("EXPLANATION")
print("==============================")
print(result["explanation"])

print("\n==============================")
print("INTERVIEW QUESTIONS")
print("==============================")
print(result["questions"])