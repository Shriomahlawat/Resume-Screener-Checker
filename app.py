
    
            import streamlit as st
import re

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("🧠 Simple Resume Analyzer App")

# --- Resume Upload or Text Input ---
upload_option = st.selectbox("Choose Input Method", ["Paste Resume Text", "Upload .txt File"])

if upload_option == "Paste Resume Text":
    resume_text = st.text_area("📄 Paste your Resume Text here", height=300)
else:
    uploaded_file = st.file_uploader("📁 Upload your Resume (.txt)", type=["txt"])
    if uploaded_file is not None:
        resume_text = uploaded_file.read().decode("utf-8")
    else:
        resume_text = ""

# --- Job Description Input ---
job_description = st.text_area("💼 Paste the Job Description here", height=200)

# --- Utility Functions ---
def extract_email(text):
    match = re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
    return match.group(0) if match else "Not Found"

def extract_phone(text):
    match = re.search(r'\b\d{10}\b', text)
    return match.group(0) if match else "Not Found"

def get_skills_score(resume, jd_keywords):
    resume_words = resume.lower().split()
    jd_words = jd_keywords.lower().split()
    match_count = sum(1 for word in jd_words if word in resume_words)
    matched_keywords = [word for word in jd_words if word in resume_words]
    return {
        "score": round((match_count / len(jd_words)) * 100, 2) if jd_words else 0,
        "matched_keywords": matched_keywords
    }

def generate_suggestions(resume, match_score, matched_keywords):
    suggestions = []

    if len(resume.split()) < 100:
        suggestions.append("🔹 Resume is too short. Try adding more details about your skills and experience.")

    if match_score < 40:
        suggestions.append("🔹 Few job description keywords are found. Include more relevant skills and keywords.")

    if extract_email(resume) == "Not Found":
        suggestions.append("🔹 Email ID is missing from the resume.")

    if extract_phone(resume) == "Not Found":
        suggestions.append("🔹 Phone number is missing or incorrectly formatted.")

    if not matched_keywords:
        suggestions.append("🔹 No relevant keywords found from job description.")

    if not suggestions:
        suggestions.append("✅ Your resume looks good! Just ensure it's tailored to each job description.")

    return suggestions

# --- Feature Computation ---
if resume_text:
    st.subheader("📋 Resume Analysis Report")

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
            result = get_skills_score(resume_text, job_description)
            st.markdown("📊 **ATS Match Score (%):**")
            st.success(f"{result['score']} % match")

            st.markdown("🔑 **Matched Keywords:**")
            st.write(", ".join(result["matched_keywords"]))
        else:
            st.info("ℹ️ Add a Job Description to calculate ATS Score.")

    # --- Suggestions ---
    if job_description:
        st.subheader("💡 Suggestions for Improvement")
        suggestions = generate_suggestions(resume_text, result['score'], result['matched_keywords'])
        for tip in suggestions:
            st.write(tip)


   
