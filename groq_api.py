import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def analyze_resume(resume_text: str, job_description: str):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a recruiter. Your job is to review a resume for a specific job opening "
                    "and assess how well the candidate matches. Be honest, detailed, and specific."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Here is the job description:\n\n{job_description}\n\n"
                    f"Here is the candidate's resume:\n\n{resume_text}\n\n"
                    "Please answer the following:\n"
                    "- How well does the resume match this job?\n"
                    "- Strengths and alignments\n"
                    "- Gaps or missing qualifications\n"
                    "- Suggestions to improve fit"
                )
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    return result['choices'][0]['message']['content']
