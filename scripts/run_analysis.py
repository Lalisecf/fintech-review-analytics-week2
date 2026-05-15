import pandas as pd

from src.preprocessing import preprocess_dataset
from src.sentiment_analysis import apply_sentiment
from src.thematic_analysis import apply_theme_analysis

# Load cleaned CSV from Task 1
df = pd.read_csv("data/raw/bank_reviews_clean.csv")

# Preprocessing
df = preprocess_dataset(df)

# Sentiment Analysis
df = apply_sentiment(df)

# Theme Analysis
df = apply_theme_analysis(df)

# Save output
df.to_csv(
    "data/processed/analyzed_reviews.csv",
    index=False
)

print("Analysis completed successfully.")