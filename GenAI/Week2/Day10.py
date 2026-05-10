import os
import time
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


models = [

    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",

    "baidu/cobuddy:free",

    "poolside/laguna-xs.2:free"
]


prompt = """
Analyze this resume.

Name: Jay

Skills:
Python, SQL, Machine Learning

Return only JSON.
"""


for model in models:

    print("\n" + "=" * 60)

    print("MODEL:", model)

    start = time.time()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    end = time.time()

    print(
        "Latency:",
        round(end - start, 2),
        "sec"
    )

    print(
        "Tokens:",
        response.usage.total_tokens
    )

    print(
        "Output:\n",
        response.choices[0].message.content
    )