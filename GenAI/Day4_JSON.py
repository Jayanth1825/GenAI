import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL_NAME = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"


prompt = """
Extract information from this resume.

Name: Jayanth,
Skills: Html, css, javascript,
Projects: BusBooking

Return ONLY valid JSON.
"""


response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


output = response.choices[0].message.content

print("Raw Output:\n")
print(output)

