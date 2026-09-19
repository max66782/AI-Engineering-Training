from agents.study_agent import study_agent
from agents.practice_agent import practice_agent
from agents.interview_agent import interview_agent


def route_request(message: str):
    message = message.lower()

    if any(word in message for word in ["study", "learn", "understand", "explain", "concept"]):
        return study_agent(message)

    if any(word in message for word in ["practice", "question", "questions", "problem", "problems", "exercise"]):
        return practice_agent(message)

    if any(word in message for word in ["interview", "mock interview", "interview me"]):
        return interview_agent(message)

    return (
    "I can help you with placement preparation. "
    "Would you like to study a concept, practice questions, "
    "or take a mock interview?"
    )