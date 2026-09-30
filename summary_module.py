from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational summarization assistant.

Summarize the following educational content:

Content:
{text}

Instructions:
- Keep the important information.
- Remove unnecessary repetition.
- Use simple language.
- Organize the result using headings or bullet points when appropriate.
- Make it useful for exam revision.
"""

    return generate_text(prompt)