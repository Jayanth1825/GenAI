import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

messages = [
    {
        "role": "system",
        "content": "You are a friendly assistant."
    },
    {
        "role": "user",
        "content": "My name is Jay."
    },
    {
        "role": "assistant",
        "content": "Nice to meet you, Jay."
    },
    {
        "role": "user",
        "content": "What is my name?"
    }
]


response = client.chat.completions.create(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    messages=messages
)

print(response.choices[0].message.content)