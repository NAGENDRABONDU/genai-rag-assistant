import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


env_path = (
    Path(__file__)
    .resolve()
    .parents[2]
    / ".env"
)

load_dotenv(
    env_path
)

api_key = os.getenv(
    "GEMINI_API_KEY"
)

if not api_key:

    raise ValueError(
        "GEMINI_API_KEY "
        "not found"
    )

client = genai.Client(
    api_key=api_key
)


def generate_response(
    prompt
):

    try:

        response = (
            client.models
            .generate_content(
                model=
                "gemini-2.5-flash",

                contents=
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