# import necessary modules
from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search


# function to get the current date in YYYY-MM-DD format
def get_current_date_and_time() -> dict:
    """
    Get the current date and time in YYYY-MM-DD format.
    :return: {"date": "YYYY-MM-DD"}
    """
    return {
        "current_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


root_agent = Agent(
    name="search_agent",

    # specify the model
    model="gemini-2.0-flash",
    description="A search tool agent to go and fetch data",

    #specify the instruction to be sent
    instruction="""
    You are a helpful and friendly assistant that can use the following tool:
    - google_search
    """,

    # specify the tool needed to be used here
    tools=[google_search],
    # tools=[get_current_date_and_time]
    # can only use one tool at a time
)
