from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

THEME_KEYWORDS = {
    "Account Access Issues": [
        "login", "password", "otp", "signin", "account"
    ],

    "Transaction Performance": [
        "transfer", "slow", "delay", "payment", "transaction"
    ],

    "UI & UX": [
        "ui", "design", "interface", "easy", "navigation"
    ],

    "Customer Support": [
        "support", "service", "response", "help", "call"
    ],

    "Feature Requests": [
        "feature", "fingerprint", "dark mode", "budget", "update"
    ]
}

def identify_theme(review):

    review = review.lower()

    for theme, keywords in THEME_KEYWORDS.items():

        for keyword in keywords:
            if keyword in review:
                return theme

    return "Other"


def apply_theme_analysis(df):

    df["identified_theme"] = df["clean_review"].apply(identify_theme)

    return df