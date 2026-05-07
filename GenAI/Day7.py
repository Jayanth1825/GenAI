import os
import json
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


MODEL_NAME = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"


st.title("AI Resume Analyzer")


resume_text = st.text_area(
    "Paste your resume here:"
)


if st.button("Analyze Resume"):

    prompt = f"""
    You are an expert HR recruiter.

    Analyze this resume.

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
                "content": "You are a strict recruiter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    output = response.choices[0].message.content


    try:

        data = json.loads(output)

        st.subheader("Analysis")

        st.json(data)


        skills = data.get("skills", [])

        score = len(skills) * 10

        st.success(
            f"Resume Score: {score}/100"
        )


    except json.JSONDecodeError:

        st.error(
            "Model did not return valid JSON."
        )