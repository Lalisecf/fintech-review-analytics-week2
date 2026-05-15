import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd

from src.preprocessing import preprocess_dataset
from src.sentiment_analysis import apply_sentiment
from src.thematic_analysis import apply_theme_analysis

# Load dataset
df = pd.read_csv("data/raw/bank_reviews_clean.csv")

# Preprocess
df = preprocess_dataset(df)

# Sentiment
df = apply_sentiment(df)

# Theme analysis
df = apply_theme_analysis(df)

# Save output
df.to_csv(
    "data/processed/analyzed_reviews.csv",
    index=False
)

print("Analysis completed successfully.")