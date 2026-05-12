import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL_NAME = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"

resume = """
Name: Jay

Skills:
Java, SpringBoot, React

Projects:
Netflix Clone, Hospital Management System

Experience:
Worked as Full Stack Developer Intern
"""

prompt_v1 = f"""
Analyze this resume.

Return JSON.

{resume}
"""

prompt_v2 = f"""
You are a strict ATS recruiter.

Analyze this software engineer resume.

Return ONLY valid JSON.

Include:
name
skills
strengths
weaknesses
missing_skills

{resume}
"""

prompt_v3 = f"""
You are a recruiter hiring backend engineers.

Evaluate:

1. Technical depth
2. Project quality
3. Industry readiness

Return ONLY valid JSON.

{resume}
"""

prompts = {
    "V1": prompt_v1,
    "V2": prompt_v2,
    "V3": prompt_v3
}

for version, prompt in prompts.items():

    print("\n" + "=" * 60)
    print(version)
    print("=" * 60)

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

    print("\nOUTPUT:\n")
    print(output)

    print("\nTOKEN USAGE:\n")
    print(response.usage)