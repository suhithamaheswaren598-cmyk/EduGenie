import os

from dotenv import load_dotenv
from google import genai


# Load the .env file
load_dotenv()


# Get the Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")


# Check whether the API key exists
if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please check your .env file."
    )


# Create Gemini client
client = genai.Client(api_key=API_KEY)


# Gemini model
MODEL_NAME = "gemini-3.5-flash-lite"


import time
from google.genai.errors import ServerError


def generate_text(prompt: str) -> str:
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            if not response.text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return response.text.strip()

        except ServerError as e:
            if attempt == 2:
                raise e

            time.sleep(3)