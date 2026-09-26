import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")

print("API key loaded:", True)

# --------------------------------------------------
# 1. Initialize Gemini through LangChain
# --------------------------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=api_key,
)

# --------------------------------------------------
# 2. Prompt Template
# --------------------------------------------------

explanation_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms for a beginner."
)

# --------------------------------------------------
# 3. Simple Chain
# --------------------------------------------------

explanation_chain = explanation_prompt | model

# --------------------------------------------------
# 4. Multi-step LCEL Chain
# --------------------------------------------------

question_prompt = ChatPromptTemplate.from_template(
    """
    Based on the following topic and explanation,
    generate 3 technical interview questions.

    Topic:
    {topic}

    Explanation:
    {explanation}
    """
)

interview_chain = (
    {
        "topic": RunnablePassthrough(),
        "explanation": explanation_prompt | model,
    }
    | question_prompt
    | model
)

# --------------------------------------------------
# 5. LangChain Tool
# --------------------------------------------------

@tool
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two integers."""
    return a + b


# --------------------------------------------------
# 6. Tool Test
# --------------------------------------------------

tool_result = calculate_sum.invoke({
    "a": 10,
    "b": 20,
})

print("\nTool Test:")
print("10 + 20 =", tool_result)

# --------------------------------------------------
# 7. Run Explanation Chain
# --------------------------------------------------

topic = "FastAPI"

explanation = explanation_chain.invoke({
    "topic": topic
})

print("\n==============================")
print("EXPLANATION")
print("==============================")
print(explanation.content)

# --------------------------------------------------
# 8. Run Multi-step Interview Chain
# --------------------------------------------------

interview_questions = interview_chain.invoke(topic)

print("\n==============================")
print("INTERVIEW QUESTIONS")
print("==============================")
print(interview_questions.content)

# --------------------------------------------------
# 9. Interactive Mode
# --------------------------------------------------

print("\n==============================")
print("AI INTERVIEW ASSISTANT")
print("==============================")

user_topic = input("\nEnter a topic for interview preparation: ")

result = interview_chain.invoke(user_topic)

print("\nInterview Questions:")
print(result.content)