import os
from dotenv import load_dotenv
from resume_utils import extract_text_from_pdf
from preprocess import clean_resume_text
from groq_api import analyze_resume

resume_text = extract_text_from_pdf("sample_resume.pdf")
cleaned = clean_resume_text(resume_text)

job_description = """
We are looking for a Junior AI Engineer with experience in Python, machine learning, and NLP. 
Familiarity with LLMs (like GPT, LLaMA), FastAPI, and cloud deployment (AWS preferred) is a plus.
"""

feedback = analyze_resume(cleaned, job_description)

print("\n=== AI Resume Feedback ===\n")
print(feedback)
