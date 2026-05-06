import os
import json
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


MODEL_NAME = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"


resume_text = """
Name: Jay

Skills:
Java, SpringBoot, React, SQL, Github

Projects:
Built an E-commerce application for a local company that has 500+ orders everyday.

Experience:
No Experience
"""


prompt = f"""
You are an expert HR recruiter.

Analyze the following resume.

Extract:
- name
- skills
- strengths
- weaknesses
- improvement_suggestions

Return ONLY valid JSON.

Resume:
{resume_text}
"""

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "system",
            "content": "You are a strict HR recruiter."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

output = response.choices[0].message.content

print("\nRAW MODEL OUTPUT:\n")
print(output)


try:

    data = json.loads(output)

    print("\nPARSED RESUME DATA:\n")

    print(json.dumps(data, indent=4))

    skills = data.get("skills", [])

    score = 0

    if "Java" in skills:
        score += 15

    if "SpringBoot" in skills:
        score += 15

    if "React" in skills:
        score += 15

    score += 20
    score += 20

    print("\nRESUME SCORE:", score)

except json.JSONDecodeError:

    print("\nERROR: Model did not return valid JSON.")