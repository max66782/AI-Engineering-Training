from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def interview_agent(message: str):
    instruction = """
    You are an Interview Agent for a placement preparation assistant.
    Your responsibility is to conduct technical mock interviews.
    Ask one question at a time.
    Wait for the student's answer before asking the next question.
    Evaluate the student's answer and provide constructive feedback.
    Adjust questions based on the student's level when possible.
    Do not act as a Study Agent or Practice Agent.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"{instruction}\n\nStudent request: {message}"
    )

    return response.text