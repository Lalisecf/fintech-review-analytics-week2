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

    text = str(text).strip()

    if len(text) == 0:
        return "neutral", 0.0

    result = classifier(text[:512])[0]

    label = result["label"].lower()
    score = result["score"]

    # Add neutral threshold
    if score < 0.75:
        sentiment = "neutral"

    elif label == "positive":
        sentiment = "positive"

    else:
        sentiment = "negative"

    return sentiment, round(score, 4)


def apply_sentiment(df):

    sentiments = df["clean_review"].apply(analyze_sentiment)

    df["sentiment_label"] = sentiments.apply(lambda x: x[0])
    df["sentiment_score"] = sentiments.apply(lambda x: x[1])

    return df