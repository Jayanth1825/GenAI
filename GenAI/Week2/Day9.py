import os
import time
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


MODEL_NAME = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"


def test_input(text):

    start = time.time()

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content":
                f"Summarize:\n{text}"
            }
        ]
    )

    end = time.time()

    print("\nLatency:",
          round(end - start, 2),
          "seconds")

    print(
        "Usage:",
        response.usage
    )

    print(
        "Output:",
        response.choices[0].message.content
    )


short_text = "Python SQL Machine Learning"


long_text = short_text * 100


print("\nSHORT INPUT")
test_input(short_text)


print("\nLONG INPUT")
test_input(long_text)