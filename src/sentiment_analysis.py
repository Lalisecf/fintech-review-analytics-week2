from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):

    score = analyzer.polarity_scores(text)

    compound = score["compound"]

    if compound >= 0.05:
        label = "positive"
    elif compound <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return label, compound


def apply_sentiment(df):

    sentiments = df["clean_review"].apply(analyze_sentiment)

    df["sentiment_label"] = sentiments.apply(lambda x: x[0])
    df["sentiment_score"] = sentiments.apply(lambda x: x[1])

    return df