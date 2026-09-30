import json
import re
from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    text = text.strip()

    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    return text.strip()


def generate_quiz(content: str):

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create exactly 3 multiple-choice questions from the content below.

CONTENT:
{content}

STRICT RULES:
1. Create exactly 3 questions.
2. Each question must have exactly 4 options.
3. Include the correct answer.
4. Include a short explanation.
5. Return ONLY valid JSON.
6. Do NOT use markdown.
7. Do NOT write anything before or after the JSON.

Use exactly this format:

[
  {{
    "question": "Question 1",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "correct_answer": "Option A",
    "explanation": "Explanation"
  }},
  {{
    "question": "Question 2",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "correct_answer": "Option B",
    "explanation": "Explanation"
  }},
  {{
    "question": "Question 3",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "correct_answer": "Option C",
    "explanation": "Explanation"
  }}
]
"""

    response = generate_text(prompt)

    cleaned = clean_json_block(response)

    try:
        quiz = json.loads(cleaned)

    except json.JSONDecodeError as e:
        print("QUIZ JSON ERROR:")
        print(cleaned)
        raise ValueError(
            "Gemini did not return valid quiz JSON."
        ) from e

    if not isinstance(quiz, list):
        raise ValueError("Quiz response must be a list.")

    if len(quiz) != 3:
        raise ValueError("Quiz must contain exactly 3 questions.")

    for question in quiz:

        if "question" not in question:
            raise ValueError("Missing question.")

        if "options" not in question:
            raise ValueError("Missing options.")

        if len(question["options"]) != 4:
            raise ValueError(
                "Each question must have exactly 4 options."
            )

        if "correct_answer" not in question:
            raise ValueError("Missing correct answer.")

        if "explanation" not in question:
            raise ValueError("Missing explanation.")

    return quiz