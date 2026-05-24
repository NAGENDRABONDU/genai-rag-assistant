import os
from pathlib import Path

from dotenv import load_dotenv
import google.generativeai as genai


env_path = (
    Path(__file__)
    .resolve()
    .parents[2]
    / ".env"
)

load_dotenv(env_path)

api_key = os.getenv(
    "GEMINI_API_KEY"
)

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found"
    )

genai.configure(
    api_key=api_key
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_response(prompt):

    try:

        response = (
            model.generate_content(
                prompt
            )
        )

        return response.text

    except Exception as e:

        print(
            "Gemini Error:",
            str(e)
        )

        return (
            "The AI service is "
            "currently unavailable. "
            "Please try again later."
        )