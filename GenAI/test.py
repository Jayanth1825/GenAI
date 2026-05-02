import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    messages=[
        {"role": "user",
         "content": "Tell about india."
        }
    ]
)

print(response.choices[0].message.content)