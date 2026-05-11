import os
import json
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


MODEL_NAME = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"


correct = 0
test_resumes = [

    """
    Name: Jay
    Skills: Java, SpringBoot, React
    """,

    """
    Name: Rahul
    Skills: Python, SQL, Machine Learning
    """,

    """
    Name: Priya
    Skills: HTML, CSS
    """
]
expected_skills = [

    ["Java", "SpringBoot", "React"],

    ["Python", "SQL", "Machine Learning"],

    ["HTML", "CSS"]
]

for i, resume in enumerate(test_resumes):

    prompt = f"""
    Extract skills.

    Return ONLY JSON.

    Resume:
    {resume}
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


    try:

        data = json.loads(output)

        predicted = data["skills"]

        expected = expected_skills[i]


        if predicted == expected:

            correct += 1

    except:

        pass


accuracy = (
    correct /
    len(test_resumes)
) * 100


print(
    "Accuracy:",
    accuracy
)