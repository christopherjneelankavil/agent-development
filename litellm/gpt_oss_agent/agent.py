# import necessary modules
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os

# Initialize the LiteLlm model with the specified Hugging Face model and API key
model = LiteLlm(
    model="huggingface/openai/gpt-oss-20b",
    api_key=os.getenv("HF_TOKEN")
)

# Create the GPT OSS Agent with the model and relevant details
root_agent = Agent(
    name="gpt_oss_agent",

    # call the model that was initialized earlier
    model=model,
    description="GPT OSS Agent",
    instruction="You are a helpful assistant that uses GPT OSS to answer user queries.",
)