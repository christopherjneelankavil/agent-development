from google.adk.agents import LlmAgent
from dotenv import load_dotenv

load_dotenv(".env")

question_answer_agent = LlmAgent(
    name="question_answer_agent",
    description="An agent that answers questions based on provided context.",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful assistant that provides accurate and concise answers to questions based on the given context.
    Here is some information about the user:
    Name : {username}
    Preferences : {user_preferences}
    """,
)