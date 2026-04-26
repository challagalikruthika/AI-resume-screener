import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from resume_parser import extract_text_from_pdf
from text_preprocessing import clean_text

# Job description (can be text file or string)
job_description = """
Looking for a Python developer with skills in
machine learning, data analysis, SQL and NLP.
"""

clean_jd = clean_text(job_description)

resume_texts = []
resume_names = []

# Read all resumes
for file in os.listdir("resumes"):
    if file.endswith(".pdf"):
        text = extract_text_from_pdf(f"resumes/{file}")
        clean_resume = clean_text(text)
        resume_texts.append(clean_resume)
        resume_names.append(file)

# Combine JD + resumes
documents = [clean_jd] + resume_texts

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Similarity scores
scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# Threshold
THRESHOLD = 0.6

print("\n Resume Ranking Results:\n")

for name, score in sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True):
    status = " Shortlisted" if score >= THRESHOLD else " Rejected"
    print(f"{name} → Score: {score:.2f} → {status}")
