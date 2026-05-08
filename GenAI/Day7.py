import os
import json
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


st.set_page_config(
    page_title="Smart AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


MODEL_NAME = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"


# HERO
st.markdown("# 📄 Smart AI Resume Analyzer")
st.caption(
    "AI-powered ATS analysis, skill gap detection, and career recommendations."
)


# SIDEBAR
with st.sidebar:

    st.header("Features")

    st.write("✅ Resume Analysis")
    st.write("✅ ATS Score")
    st.write("✅ Skill Gap Detection")
    st.write("✅ Career Suggestions")


# FILE INPUT
uploaded_file = st.file_uploader(
    "Upload Resume (.txt)",
    type=["txt"]
)


if uploaded_file:

    resume_text = uploaded_file.read().decode()


    if st.button("Analyze Resume"):

        prompt = f"""
        Analyze this resume.

        Return JSON:

        {{
            "name":"",
            "skills":[],
            "strengths":[],
            "weaknesses":[],
            "missing_skills":[],
            "job_roles":[],
            "experience":""
        }}

        Resume:
        {resume_text}
        """


        with st.spinner("Running AI analysis..."):

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a strict ATS recruiter."
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

            skills = data.get("skills", [])

            score = min(
                len(skills) * 20,
                100
            )

            ats_score = min(
                score + 10,
                100
            )


            # KPI CARDS
            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Resume Score",
                f"{score}/100"
            )

            c2.metric(
                "ATS Score",
                f"{ats_score}/100"
            )

            c3.metric(
                "Skills",
                len(skills)
            )

            c4.metric(
                "Experience",
                data.get(
                    "experience",
                    "N/A"
                )
            )


            st.progress(score / 100)


            # ANALYSIS
            left, right = st.columns(2)


            with left:

                st.subheader("💪 Strengths")

                for item in data.get(
                        "strengths", []
                ):
                    st.success(item)


            with right:

                st.subheader("⚠ Weaknesses")

                for item in data.get(
                        "weaknesses", []
                ):
                    st.error(item)


            # SKILL GAP
            st.subheader("📚 Missing Skills")

            for item in data.get(
                    "missing_skills", []
            ):
                st.info(item)


            # JOB ROLES
            st.subheader("🚀 Suggested Roles")

            for item in data.get(
                    "job_roles", []
            ):
                st.write("•", item)


            with st.expander(
                    "View Raw JSON"
            ):
                st.json(data)


        except:

            st.error(
                "Invalid JSON returned."
            )