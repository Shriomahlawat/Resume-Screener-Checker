import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import numpy as np

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\\s]', '', text)
    return text

def skill_score(resume_text, jd_text):
    resume_clean = preprocess(resume_text)
    jd_clean = preprocess(jd_text)
    X = vectorizer.transform([resume_clean, jd_clean])
    score = np.dot(X[0].toarray(), X[1].toarray().T)[0][0]
    return score * 100

def experience_level(text):
    experience_keywords = {
        "Intern": ["internship", "trainee"],
        "Entry-Level": ["0-1 years", "fresher", "graduate"],
        "Mid-Level": ["2-5 years", "associate", "developer"],
        "Senior-Level": ["5+ years", "lead", "senior", "manager"]
    }
    text = preprocess(text)
    for level, keywords in experience_keywords.items():
        if any(keyword in text for keyword in keywords):
            return level
    return "Unknown"

def keyword_gap(resume_text, jd_text):
    resume_words = set(preprocess(resume_text).split())
    jd_words = set(preprocess(jd_text).split())
    missing = jd_words - resume_words
    return list(missing)[:20]
