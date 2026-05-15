import pdfplumber
import re
import nltk
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))


def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text


def clean_resume_text(text):

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove emails
    text = re.sub(r"\S+@\S+", "", text)

    # Remove special characters
    text = re.sub(r"[^A-Za-z0-9 ]+", " ", text)

    # Lowercase
    text = text.lower()

    # Remove stopwords
    words = text.split()

    filtered_words = [
        word for word in words
        if word not in STOPWORDS
    ]

    cleaned_text = " ".join(filtered_words)

    return cleaned_text