from openai import OpenAI
from config.config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_test_cases(requirement):
    prompt = f"""
    You are a QA expert.
    Generate detailed test cases including:
    - Positive scenarios
    - Negative scenarios
    - Edge cases

    Requirement:
    {requirement}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
