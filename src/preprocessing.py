import pandas as pd
import re
import spacy
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove punctuation
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Tokenization + Lemmatization
    doc = nlp(text)

    tokens = [
        token.lemma_
        for token in doc
        if token.text not in stop_words
        and not token.is_punct
        and not token.is_space
    ]

    return " ".join(tokens)

def preprocess_dataset(df):
    df = df.dropna(subset=["review", "rating"])

    df["clean_review"] = df["review"].apply(clean_text)

    return df