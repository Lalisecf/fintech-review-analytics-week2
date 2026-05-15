from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

THEME_KEYWORDS = {

    "Account Access Issues": [
        "login",
        "password",
        "otp",
        "signin",
        "account",
        "verification",
        "authenticate"
    ],

    "Transaction Performance": [
        "transfer",
        "slow",
        "delay",
        "payment",
        "transaction",
        "loading",
        "failed",
        "crash",
        "error"
    ],

    "UI & UX": [
        "ui",
        "design",
        "interface",
        "easy",
        "navigation",
        "smooth",
        "friendly"
    ],

    "Customer Support": [
        "support",
        "service",
        "response",
        "help",
        "call",
        "agent",
        "customer care"
    ],

    "Feature Requests": [
        "feature",
        "fingerprint",
        "dark mode",
        "budget",
        "update",
        "biometric",
        "notification"
    ]
}


def identify_theme(review):

    # Handle missing reviews
    if pd.isna(review):
        return "Other"

    review = str(review).lower()

    for theme, keywords in THEME_KEYWORDS.items():

        for keyword in keywords:

            if keyword in review:
                return theme

    return "Other"


def apply_theme_analysis(df):

    df["identified_theme"] = (
        df["clean_review"]
        .apply(identify_theme)
    )

    return df


def extract_keywords(df, top_n=20):

    """
    Extract top keywords and n-grams using TF-IDF
    """

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),   # unigram + bigram
        max_features=top_n
    )

    tfidf_matrix = vectorizer.fit_transform(
        df["clean_review"]
    )

    keywords = vectorizer.get_feature_names_out()

    scores = tfidf_matrix.sum(axis=0).A1

    keyword_df = pd.DataFrame({
        "keyword": keywords,
        "score": scores
    })

    keyword_df = keyword_df.sort_values(
        by="score",
        ascending=False
    )

    return keyword_df