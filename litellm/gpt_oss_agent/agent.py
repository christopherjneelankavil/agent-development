from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os

model = LiteLlm(
    model="huggingface/openai/gpt-oss-20b",
    api_key=os.getenv("HF_TOKEN")
)

root_agent = Agent(
    name="gpt_oss_agent",
    model=model,
    description="GPT OSS Agent",
    instruction="You are a helpful assistant that uses GPT OSS to answer user queries.",
)