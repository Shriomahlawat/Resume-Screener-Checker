# app.py

import streamlit as st
import re

# Required skill list for matching
REQUIRED_SKILLS = ['Python', 'Machine Learning', 'SQL', 'Git', 'AWS']

# Education Levels
EDUCATION_LEVELS = {
    "Ph.D": ["ph.d", "doctor of philosophy"],
    "Master's": ["master", "m.sc", "m.tech", "mba"],
    "Bachelor's": ["bachelor", "b.tech", "b.sc", "b.e"]
}


def extract_text(file):
    return file.read().decode('utf-8')


def skill_match(resume_text):
    matched = [skill for skill in REQUIRED_SKILLS if skill.lower() in resume_text.lower()]
    return matched, list(set(REQUIRED_SKILLS) - set(matched))


def detect_education_level(resume_text):
    text = resume_text.lower()
    for level, keywords in EDUCATION_LEVELS.items():
        for keyword in keywords:
            if keyword in text:
                return level
    return "Not Found"


def estimate_experience(resume_text):
    years = re.findall(r'(\d+)\+?\s+years', resume_text.lower())
    if years:
        max_year = max(map(int, years))
        if max_year >= 5:
            return "Senior Level"
        elif max_year >= 2:
            return "Mid Level"
        else:
            return "Entry Level"
    return "Not Mentioned"


# ---------------------- Streamlit App ----------------------

st.title("📄 Simple Resume Analyzer")
st.write("Upload a plain text `.txt` resume to get analysis.")

uploaded_file = st.file_uploader("Upload Resume (.txt only)", type=["txt"])

if uploaded_file is not None:
    resume_text = extract_text(uploaded_file)

    st.subheader("✅ Skill Match")
    matched_skills, missing_skills = skill_match(resume_text)
    st.write("**Matched Skills:**", matched_skills)
    st.write("**Missing Skills:**", missing_skills)

    st.subheader("🎓 Education Level")
    education = detect_education_level(resume_text)
    st.write("**Detected Education:**", education)

    st.subheader("💼 Experience Level")
    experience = estimate_experience(resume_text)
    st.write("**Estimated Level:**", experience)

    st.success("Analysis Complete ✅")
