from sklearn.feature_extraction.text import TfidfVectorizer
from text_preprocessing import clean_text

# Sample resume text
resume_text = """
Python developer with experience in machine learning,
data analysis and SQL projects.
"""

# Sample job description text
job_description = """
Looking for a Python developer skilled in machine learning,
data analysis, SQL and NLP.
"""

# Clean both texts
clean_resume = clean_text(resume_text)
clean_jd = clean_text(job_description)

# Convert to list (IMPORTANT)
documents = [clean_resume, clean_jd]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print("TF-IDF Matrix:\n")
print(tfidf_matrix.toarray())

print("\nFeature Names (Words):\n")
print(vectorizer.get_feature_names_out())
from sklearn.metrics.pairwise import cosine_similarity

# Calculate similarity
similarity_score = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:2]
)

print("\nCosine Similarity Score:")
print(similarity_score[0][0])

