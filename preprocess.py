import re

def clean_resume_text(raw_text: str) -> str:
    text = re.sub(r' \n+', '\n', raw_text)  #Remove extra spaces before newlines
    text = re.sub(r'[ \t]+', ' ', text) #Remove extra spaces and tabs
    text = text.strip() #Remove leading and trailing spaces

    replacements = {
        r'(?i)(education)': '\n## Education\n',
        r'(?i)(experience|work history|professional experience)': '\n## Experience\n',
        r'(?i)(skills|technical skills)': '\n## Skills\n',
        r'(?i)(certifications|certificates)': '\n## Certifications\n',
        r'(?i)(projects|project experience)': '\n## Projects\n'
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)

    return text 