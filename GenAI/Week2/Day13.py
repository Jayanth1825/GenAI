import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL_NAME = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"

resume = """
Name: Jay

Skills:
Python, ML, TensorFlow, PyTorch

Projects:
Built an E-mail Spam detection using Machine Learning concepts.

Experience:
No Prior Experience in IT Industry.
"""

prompt = f"""
Analyze the given resume for ML Engineer.

Extract:

name
skills
projects
experience

Return ONLY valid JSON.

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

data = json.loads(output)

skills = data.get("skills", [])

projects = data.get("projects", [])

experience = data.get("experience", "")

backend_skills = [
    "Python",
    "ML",
    "TensorFlow",
    "PyTorch",
    "SQL",
    "Docker",
    "AWS",
    "Git",
    "REST APIs"
]

matched_skills = []
missing_skills = []

for skill in backend_skills:

    if skill in skills:
        matched_skills.append(skill)

    else:
        missing_skills.append(skill)

score = 0

score += len(matched_skills) * 10

if len(projects) >= 2:
    score += 20

if experience:
    score += 20

if score > 100:
    score = 100

recommendations = []

if "SQL" in missing_skills:
    recommendations.append(
        "Learn SQL and database design."
    )

if "Docker" in missing_skills:
    recommendations.append(
        "Learn Docker and containerization."
    )

if "AWS" in missing_skills:
    recommendations.append(
        "Learn AWS cloud fundamentals."
    )

if "Git" in missing_skills:
    recommendations.append(
        "Practice Git and GitHub workflows."
    )

if "REST APIs" in missing_skills:
    recommendations.append(
        "Build REST API projects."
    )

print("\n" + "=" * 60)
print("RESUME ANALYSIS")
print("=" * 60)

print("\nName:")
print(data["name"])

print("\nSkills:")
print(skills)

print("\nMatched Skills:")
print(matched_skills)

print("\nMissing Skills:")
print(missing_skills)

print("\nResume Score:")
print(f"{score}/100")

print("\nRecommendations:")
for item in recommendations:
    print("-", item)