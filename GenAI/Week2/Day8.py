import os
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


MODEL_NAME = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"


long_prompt = """
You are a highly experienced recruiter with many years of experience.

Please carefully analyze the following resume and provide professional feedback.

Return strengths, weaknesses, and suggestions.

Resume:
Jay knows Python, SQL, ML.
"""


short_prompt = """
Analyze this resume.

Return strengths, weaknesses, suggestions.

Jay knows Python, SQL, ML.
"""


def ask(prompt):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response


# Long Prompt
long_response = ask(long_prompt)


# Short Prompt
short_response = ask(short_prompt)


print("LONG PROMPT RESPONSE:\n")
print(
    long_response.choices[0].message.content
)


print("\nSHORT PROMPT RESPONSE:\n")
print(
    short_response.choices[0].message.content
)

print(long_response.usage)
print(short_response.usage)