import nltk
import string
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ''.join([char for char in text if not char.isdigit()])
    stop_words = set(stopwords.words('english'))
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

sample_text = """
Name: Kruthika
Skills: Python, Machine Learning, SQL
Education: B.Tech CSE AI DS
"""

cleaned_text = clean_text(sample_text)
print(cleaned_text)
