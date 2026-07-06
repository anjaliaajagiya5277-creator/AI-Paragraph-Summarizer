import os
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-2.5-flash"


def summarize_text(text):

    prompt = f"""
You are an expert AI Text Summarizer.

Summarize the following paragraph.

Rules:

• Keep the original meaning.
• Use simple English.
• Make it concise.
• Maximum 120 words.
• Do not add new information.

Paragraph:

{text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text