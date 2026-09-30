from gemini_client import generate_text


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.

Question:
{question}

Instructions:
- Use simple language.
- Explain the answer clearly.
- Give an example when useful.
- Avoid unnecessary complexity.
- If the question is academic, structure the answer logically.
"""

    return generate_text(prompt)