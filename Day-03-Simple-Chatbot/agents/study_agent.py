from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def study_agent(message: str):
    instruction = """
    You are a Study Agent for a placement preparation assistant.
    Your responsibility is to help students understand technical concepts.
    Explain concepts clearly and simply.
    Assume the student is a beginner.
    Use examples when helpful.
    Do not conduct mock interviews or generate practice tests.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"{instruction}\n\nStudent request: {message}"
    )

    return response.text