import streamlit as st
from resume_utils import extract_text_from_pdf
from preprocess import clean_resume_text
from groq_api import analyze_resume
import tempfile

st.set_page_config(page_title = "AI Resume Feedback", layout = "wide")
st.title("AI-Powered Resume Analyzer")
st.markdown("Upload your resume in PDF format and get AI-generated feedback.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type = ["pdf"])

job_description = st.text_area("Paste the job description here", height = 200)

if uploaded_file and job_description:
    with st.spinner("Processing..."):
        with tempfile.NamedTemporaryFile(delete = False, suffix = ".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        
        resume_text = extract_text_from_pdf(tmp_path)
        cleaned_text = clean_resume_text(resume_text)

        feedback = analyze_resume(cleaned_text, job_description)

    st.markdown("### AI Feedback")
    st.write(feedback)