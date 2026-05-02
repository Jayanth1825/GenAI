import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def ask(prompt):
    response = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


prompts = {

    "zero_shot":
        "Classify the following product as either a 'Laptop' or 'Smartphone': 'A portable device with a large screen and keyboard for computing tasks.",

    "few_shot":
        """
Topic: Python
Explanation: Programming language.

Topic: SQL
Explanation: Database query language.

Topic: Machine Learning
Explanation:
        """,
}


for name, prompt in prompts.items():

    print(f"\n{name.upper()}")
    print("-" * 50)

    output = ask(prompt)

    print(output)