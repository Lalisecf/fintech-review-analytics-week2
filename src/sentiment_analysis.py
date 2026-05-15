from transformers import pipeline
import pandas as pd

# Load transformer model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):

    # Handle missing values
    if pd.isna(text):
        return "neutral", 0.0

    result = classifier(str(text[:512]))[0]

    label = result["label"].lower()
    score = result["score"]

    # Convert labels
    if label == "positive":
        sentiment = "positive"
        confidence = score

    elif label == "negative":
        sentiment = "negative"
        confidence = -score

    else:
        sentiment = "neutral"
        confidence = score

    return sentiment, confidence


def apply_sentiment(df):

    sentiments = df["clean_review"].apply(analyze_sentiment)

    df["sentiment_label"] = sentiments.apply(lambda x: x[0])
    df["sentiment_score"] = sentiments.apply(lambda x: x[1])

    return df