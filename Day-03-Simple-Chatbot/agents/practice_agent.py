from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def practice_agent(message: str):
    instruction = """
    You are a Practice Agent for a placement preparation assistant.
    Your responsibility is to help students practice technical concepts.
    Generate relevant practice questions based on the student's request.
    Adjust the difficulty to the student's level when possible.
    Provide answers or solutions only when requested.
    Do not explain concepts as a Study Agent or conduct mock interviews.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"{instruction}\n\nStudent request: {message}"
    )

    return response.text