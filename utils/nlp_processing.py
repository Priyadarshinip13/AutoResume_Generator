import spacy
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import re

nlp = spacy.load("en_core_web_lg")
stop_words = stopwords.words("english")

def analyze_resume(text):
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    education = [ent.text for ent in doc.ents if ent.label_ == "EDUCATION"]
    experience = re.findall(r"\d+\+? years?", text)
    return skills, experience, education

def compare_with_job_description(resume_text, job_desc):
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf = vectorizer.fit_transform([resume_text, job_desc])
    keywords = vectorizer.get_feature_names_out()
    missing_keywords = [
        word for word in job_desc.split()
        if word.lower() in keywords and word.lower() not in resume_text.lower()
    ]
    score = int(((len(keywords) - len(missing_keywords)) / len(keywords)) * 100)
    return missing_keywords, score
