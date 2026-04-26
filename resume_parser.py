import PyPDF2
from docx import Document
import os

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Test with one resume
file_path = "resumes/dummy_resume.pdf"  # change filename

if file_path.endswith(".pdf"):
    resume_text = extract_text_from_pdf(file_path)
elif file_path.endswith(".docx"):
    resume_text = extract_text_from_docx(file_path)
else:
    resume_text = "Unsupported file format"

print(resume_text)
