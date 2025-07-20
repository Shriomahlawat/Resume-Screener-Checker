import streamlit as st
from resume_parser import extract_text_from_pdf
from utils import skill_score, experience_level, keyword_gap

st.set_page_config(page_title="Resume Checker", layout="wide")

st.title("📄 Resume Checker with JD Matching 🔍")

st.sidebar.header("Upload Files")
resume_file = st.sidebar.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_file = st.sidebar.file_uploader("Upload Job Description (TXT)", type=["txt"])

if resume_file and jd_file:
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = jd_file.read().decode("utf-8")

    st.subheader("🔍 Resume Preview")
    st.text_area("Resume Text", resume_text[:1000] + "...", height=200)

    st.subheader("📌 Job Description Preview")
    st.text_area("Job Description", jd_text[:1000] + "...", height=200)

    st.subheader("✅ Skill Score")
    score = skill_score(resume_text, jd_text)
    st.success(f"Skill Match Score: {score:.2f}%")

    st.subheader("🎯 Experience Level Detection")
    exp = experience_level(resume_text)
    st.info(f"Detected Level: {exp}")

    st.subheader("🧩 Keyword Gap Analysis")
    missing_keywords = keyword_gap(resume_text, jd_text)
    if missing_keywords:
        st.warning("Keywords missing in resume:")
        st.write(", ".join(missing_keywords))
    else:
        st.success("Great! All JD keywords are present in resume.")
else:
    st.info("👈 Upload both Resume and JD files to start analysis.")
