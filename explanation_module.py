from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_PATH = "./lamini_model"

print("Loading LaMini model for Explanation module...")

tokenizer = AutoTokenizer.from_pretrained(
    "MBZUAI/LaMini-Flan-T5-783M"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

print("LaMini Explanation model loaded successfully!")


def explain_topic(topic: str) -> str:
    prompt = f"""
Explain the following topic to a student in simple English.

Topic:
{topic}

Instructions:
- Start with a simple definition.
- Explain the concept step by step.
- Use simple language.
- Give a practical example.
- Mention important points.
- Assume the learner is a beginner.
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        num_beams=4,
        early_stopping=True
    )

    result = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return result.strip()
