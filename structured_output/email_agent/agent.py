from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

# define the structured output of the model
# the class EmailResponse inherits from BaseModel which allows for easy serialization and validation
# BaseModel is a part of the Pydantic library which is used for data parsing and validation using Python type annotations

class EmailResponse(BaseModel):
    # the model will generate a subject and a body for the email
    # subject with return type str
    subject : str = Field(
        description="The subject line of the email. Should be short, professional and meaningful."
    )
    # body with return type str
    body : str = Field(
        description="The main content of the email. Should be clear, professional and well-formatted, with proper greetings, paragraphs and sign-off."
    )


# define the email agent
root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.5-flash",
    description="An agent that composes professional emails based on user prompts.",
    instruction="""
    You are an expert email composer. 
    You will receive a prompt describing the purpose and content of an email.
    Your task is to generate a professional email with a clear subject line and well-structured body.
    Ensure the email is polite, concise, and free of grammatical errors.
    
    GUIDELINES:
    - The subject should be brief, relevant to the email content, and engaging.
    - Write a well structured body with:
      * A polite and professional greeting.
      * A clear introduction stating the purpose of the email.
      * Well-organized paragraphs that cover all necessary points.
      * A courteous closing statement.
      * A professional sign-off (e.g., "Best regards," "Sincerely,").
      * Your name as signature (if applicable).
    - Suggest relevant attachments if applicable or if mentioned in the prompt.
    - Email tone should match the context (formal/informal) as per the prompt.
    - Avoid using jargon or complex language; keep it simple and to the point.
    - Proofread the email for clarity and correctness before finalizing.
    
    IMPORTANT: The resposse MUST be in the following JSON format:
    {
        "subject": "<subject line>",
        "body": "<email body>"
    }
    DO NOT include any additional text outside the JSON structure.
    """,

    # specify the output schema and key
    output_schema=EmailResponse,
    # the output will be stored under the key "email_response"
    output_key="email_response",
)



