import streamlit as st
import re

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("🧠 Simple Resume Analyzer App")

# --- User Inputs ---
resume_text = st.text_area("Paste your Resume Text here", height=300)
job_description = st.text_area("Paste the Job Description here (for ATS Score)", height=200)

# --- Utility Functions ---
def get_skills_score(resume, jd_keywords):
    resume_words = resume.lower().split()
    jd_words = jd_keywords.lower().split()
    match_count = sum(1 for word in jd_words if word in resume_words)
    return round((match_count / len(jd_words)) * 100, 2) if jd_words else 0

def extract_email(resume):
    match = re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', resume)
    return match.group(0) if match else "Not Found"

def extract_phone(resume):
    match = re.search(r'\b\d{10}\b', resume)
    return match.group(0) if match else "Not Found"

# --- Feature Computations ---
if resume_text:
    st.subheader("📋 Resume Screening Results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("✅ **Email ID:**")
        st.write(extract_email(resume_text))

        st.markdown("✅ **Phone Number:**")
        st.write(extract_phone(resume_text))

        st.markdown("📏 **Resume Length (words):**")
        st.write(len(resume_text.split()))

    with col2:
        if job_description:
            st.markdown("📊 **ATS Match Score (%):**")
            score = get_skills_score(resume_text, job_description)
            st.success(f"{score} % match with job description")

            st.markdown("🔑 **Matching Keyword Count:**")
            jd_keywords = job_description.lower().split()
            matched_keywords = [word for word in jd_keywords if word in resume_text.lower().split()]
            st.write(len(matched_keywords))
        else:
            st.info("Add a Job Description to calculate ATS Score.")







   
