from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
You are EduGenie, a personalized learning assistant.

Create a learning path for:

Topic:
{topic}

Structure the response as:

1. Beginner Level
2. Basic Concepts
3. Intermediate Level
4. Advanced Level
5. Practice Activities
6. Recommended Resources
7. Suggested Timeline
8. Final Project

For every level:
- Explain what to learn.
- Give practical suggestions.
- Mention useful resources where appropriate.
- Keep the roadmap realistic for a student.

Use simple and clear language.
"""

    return generate_text(prompt)