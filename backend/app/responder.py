from openai import OpenAI
from .config import OPENAI_API_KEY, MODEL_NAME
from .prompt_builder import build_system_prompt, build_user_prompt

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(question: str, retrieved: dict, language: str):
    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "system", "content": build_system_prompt(language)},
            {"role": "user", "content": build_user_prompt(question, retrieved)}
        ]
    )
    return response.output_text
