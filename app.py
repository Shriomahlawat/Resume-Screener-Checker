import streamlit as st
import re

# Define job-related keywords
keywords = ["python", "machine learning", "sql", "data analysis", "communication", "excel"]

# Title
st.title("📄 Simple Resume Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload your resume (.txt format)", type=["txt"])

if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8").lower()
    st.subheader("🔍 Resume Analysis")

    # Feature 1: Keyword Match Score
    matched_keywords = [kw for kw in keywords if kw in resume_text]
    score = len(matched_keywords) / len(keywords) * 100
    st.write("✅ **Keyword Match Score:**", f"{score:.2f}%")
    st.write("Matched Keywords:", ", ".join(matched_keywords) if matched_keywords else "None")

    # Feature 2: Experience Level Estimation
    years = re.findall(r'(\d+)\s+years?', resume_text)
    if years:
        max_years = max(map(int, years))
        if max_years >= 5:
            level = "Senior"
        elif max_years >= 2:
            level = "Mid-Level"
        else:
            level = "Junior"
    else:
        level = "Not Specified"

    st.write("👔 **Experience Level:**", level)
