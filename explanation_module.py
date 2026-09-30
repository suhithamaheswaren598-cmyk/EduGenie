from gemini_client import generate_text


def explain_topic(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Explain the following topic clearly for a student:

Topic:
{topic}

Instructions:
- Start with a simple definition.
- Explain the concept step by step.
- Use simple and easy-to-understand language.
- Give a practical or real-world example when useful.
- Include important points for exam preparation.
- Use headings and bullet points where appropriate.
- Avoid unnecessary complexity.
"""

    return generate_text(prompt)