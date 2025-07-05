# 🧠 AI-Powered Resume Analyzer

An intelligent, open-source web app that analyzes your resume using Groq's blazing-fast LLaMA 3 API.  
Upload your resume, paste a job description, and receive instant, GPT-style feedback — strengths, gaps, and improvement suggestions.

<p align="center">
  <img src="https://img.shields.io/badge/built_with-Streamlit-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/LLM-Groq%20LLaMA3-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/PDF-Resume%20Parser-green?style=flat-square"/>
</p>

---

## 🚀 Features

- 📄 Upload resume as PDF
- 📝 Paste job description text
- ⚡ Lightning-fast feedback with **Groq + LLaMA 3**
- 💬 AI feedback: strengths, weaknesses, and suggestions
- 🧠 Prompt-engineered LLM evaluation logic
- 🖥️ Simple Streamlit web UI

---

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
| LLM | Groq API with `llama3-70b-8192` |
| UI  | Streamlit |
| PDF Parsing | PyMuPDF |
| Env Management | `python-dotenv` |
| Core Language | Python 3.11 |

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git
cd resume-analyzer
