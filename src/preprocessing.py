import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()

def clean_text(text):

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove punctuation/numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    tokens = text.split()

    cleaned_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(cleaned_tokens)


def preprocess_dataset(df):

    df = df.dropna(subset=["review", "rating"])

    df["clean_review"] = df["review"].apply(clean_text)

    return df