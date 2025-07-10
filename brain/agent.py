import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_jarvis(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']