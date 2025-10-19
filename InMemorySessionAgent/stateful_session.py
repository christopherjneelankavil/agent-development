from dotenv import load_dotenv
from litellm import uuid

from question_answer_agent import question_answer_agent
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.adk.runners import Runner

# load environment variables from .env file
load_dotenv(".env")

# create a new session to store state
session_service = InMemorySessionService()

initial_state = {
    "name" : "John Doe",
    "user_preferences" : "loves hiking and outdoor activities, enjoys reading science fiction novels, and is a foodie who likes to explore new cuisines.",
}

# create new session with initial state
APP_NAME="stateful_qa_app"
USER_ID="user_123"
SESSION_ID=str(uuid.uuid4())

# create session
stateful_session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state
)

print("----------------------------------------------------")
print("|      CREATED NEW SESSION WITH INITIAL STATE      |")
print("|                                                  |")
print(f"| Session ID: {SESSION_ID}|")
print("----------------------------------------------------")

# create a runner to execute the agent within the session
runner = Runner(
    agent=question_answer_agent,
    app_name=APP_NAME,
    session_service=session_service
)