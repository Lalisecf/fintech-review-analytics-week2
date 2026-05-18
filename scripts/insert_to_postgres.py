import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# ==========================================
# DATABASE CONNECTION
# ==========================================

DB_USER = "postgres"
DB_PASSWORD = "Ginbot21990@"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "bank_reviews"

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
)

engine = create_engine(DATABASE_URL)

# ==========================================
# LOAD CLEANED DATA
# ==========================================

df = pd.read_csv("data/processed/analyzed_reviews.csv")

# ==========================================
# INSERT BANKS
# ==========================================

banks = df[['bank', 'bank']].drop_duplicates()
banks.columns = ['bank_name', 'app_name']

banks.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)

# ==========================================
# GET BANK IDS
# ==========================================

bank_df = pd.read_sql("SELECT * FROM banks", engine)

bank_mapping = dict(
    zip(bank_df['bank_name'], bank_df['bank_id'])
)

# ==========================================
# PREPARE REVIEWS TABLE
# ==========================================

df['bank_id'] = df['bank'].map(bank_mapping)

reviews_df = df[[
    'bank_id',
    'review',
    'rating',
    'date',
    'sentiment_label',
    'sentiment_score',
    'identified_theme',
    'source'
]]

reviews_df.columns = [
    'bank_id',
    'review_text',
    'rating',
    'review_date',
    'sentiment_label',
    'sentiment_score',
    'identified_theme',
    'source'
]

# ==========================================
# INSERT REVIEWS
# ==========================================

reviews_df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully!")