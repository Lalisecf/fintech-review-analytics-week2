from src.sentiment_analysis import analyze_sentiment

def test_positive_sentiment():

    label, score = analyze_sentiment(
        "This app is excellent and fast"
    )

    assert label == "positive"
    assert score > 0.5