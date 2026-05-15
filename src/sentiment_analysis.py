from transformers import pipeline
import pandas as pd

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):

    if not text or len(text.strip()) == 0:
        return "neutral", 0.0

    result = classifier(text[:512])[0]

    label = result["label"]
    score = result["score"]

    if label == "POSITIVE":
        sentiment = "positive"
    else:
        sentiment = "negative"

    return sentiment, score


def apply_sentiment(df):

    sentiments = df["clean_review"].apply(analyze_sentiment)

    df["sentiment_label"] = sentiments.apply(lambda x: x[0])
    df["sentiment_score"] = sentiments.apply(lambda x: x[1])

    return df