from pdfminer.high_level import extract_text
import docx
import re

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def parse_resume(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

def extract_skills(text):
    # Example regex for skills extraction (customize as needed)
    skills_pattern = r'\b(?:Python|Java|JavaScript|C\+\+|SQL|HTML|CSS|React|Node\.js|Django|Flask|Machine Learning|AI)\b'
    return list(set(re.findall(skills_pattern, text, re.IGNORECASE)))

def extract_keywords(text):
    # Example keywords extraction logic (customize as needed)
    keywords = text.split()
    return list(set(keywords))

def suggest_job_roles(skills):
    # Example job role suggestions based on skills (customize as needed)
    job_roles = {
        'Python': 'Python Developer',
        'Java': 'Java Developer',
        'JavaScript': 'Frontend Developer',
        'Machine Learning': 'Data Scientist',
    }
    suggestions = []
    for skill in skills:
        if skill in job_roles:
            suggestions.append(job_roles[skill])
    return list(set(suggestions))