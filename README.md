# Fintech Review Analytics

## Customer Experience Analytics for Fintech Apps

This project analyzes customer reviews from Ethiopian mobile banking applications using data engineering and Natural Language Processing (NLP) techniques.

The goal is to transform raw Google Play Store reviews into actionable insights that help banks improve customer experience, identify recurring issues, and prioritize product improvements.

---

# Task 1: Data Collection and Preprocessing

## Objective

Collect, clean, and preprocess Google Play Store reviews from Ethiopian banking applications to create an analysis-ready dataset.

---

## Banks Included

- Commercial Bank of Ethiopia
- Bank of Abyssinia
- Dashen Bank

---

## Tools and Technologies Used

- Python
- pandas
- google-play-scraper
- Jupyter Notebook
- Git & GitHub
- GitHub Actions (CI/CD)
- pytest

---

## Project Structure

```bash
fintech-review-analytics/
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   ├── raw/
│   │   └── fintech_reviews_cleaned.csv
│   │
│   └── processed/
│       └── analyzed_reviews.csv
│
├── notebooks/
│   ├── __init__.py
│   ├── task_1_data_collection_preprocessing.ipynb
│   ├── task_2_analysis.ipynb
│   └── README.md
│
├── scripts/
│   ├── __init__.py
│   └── run_analysis.py
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── sentiment_analysis.py
│   └── thematic_analysis.py
│
├── tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_sentiment_analysis.py
│   └── test_theme.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Data Collection Methodology

Google Play Store reviews were collected using the `google-play-scraper` Python library.

### Scraping Configuration

- Country: Ethiopia (`et`)
- Language: English (`en`)
- Sorting Method: Newest Reviews
- Reviews Collected Per Bank: 500
- Total Reviews Collected: 1,500

### Fields Collected

- Review Text
- Rating (1–5)
- Review Date
- Bank Name
- Source

### Source

Google Play Store

---

# Data Preprocessing

The collected reviews were cleaned and standardized using pandas.

### Preprocessing Steps

- Removed duplicate reviews using `review_id`
- Handled missing values in review and rating columns
- Normalized dates into `YYYY-MM-DD` format
- Exported a clean CSV dataset for analysis

---

# Data Quality Assessment

### Missing Values

No missing values were found in the dataset.

### Duplicate Reviews

No duplicate reviews were detected.

### Final Dataset Summary

- Total Reviews: 1,500
- Total Columns: 5

### Reviews Per Bank

| Bank | Reviews |
|---|---|
| Commercial Bank of Ethiopia | 500 |
| Bank of Abyssinia | 500 |
| Dashen Bank | 500 |

The dataset satisfies the project requirement of collecting at least 400 reviews per bank.

---

# Final Dataset Columns

The cleaned dataset contains the following columns:

- review
- rating
- date
- bank
- source

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Scrape Reviews

```bash
python scripts/scrape_reviews.py
```

## Preprocess Reviews

```bash
python scripts/preprocess_reviews.py
```

## Run Unit Tests

```bash
pytest
```

---

# Sample Review Examples

| Review | Rating | Bank |
|---|---|---|
| "its amazing app, visually stunning" | 5 | Dashen Bank |
| "what is wrong these app ?" | 1 | Bank of Abyssinia |
| "the app does not show my account balance correctly" | 1 | Bank of Abyssinia |

The dataset contains both positive and negative customer experiences, making it suitable for sentiment and thematic analysis.

---

# Conclusion

Task 1 was completed successfully.

A total of 1,500 Google Play Store reviews were collected from:

- Commercial Bank of Ethiopia
- Bank of Abyssinia
- Dashen Bank

The dataset was cleaned by:

- Removing duplicate reviews
- Handling missing values
- Standardizing date formats
- Verifying data quality

The final cleaned dataset is balanced across all three banks and ready for:

- Sentiment Analysis
- Thematic Analysis
- PostgreSQL Database Storage
- Visualization and Business Insights

---

# Limitations

- Google Play Store may limit accessible reviews
- Some reviews are short and less descriptive
- Only English-language reviews were collected
- Review availability depends on public Google Play data

---

# Task 2: Sentiment and Thematic Analysis

## Objective

Analyze customer reviews using Natural Language Processing (NLP) techniques to identify customer sentiment, recurring issues, satisfaction drivers, and feature requests across Ethiopian mobile banking applications.

---

# Sentiment Analysis

## Model Used

The project uses the Hugging Face transformer model:

```python
distilbert-base-uncased-finetuned-sst-2-english
```

This transformer model was selected because it provides higher accuracy and better contextual understanding than traditional lexicon-based sentiment analysis methods such as VADER or TextBlob.

The model classifies each review into:

- Positive
- Negative
- Neutral

A confidence score is also generated for each prediction.

---

## Sentiment Analysis Pipeline

The sentiment analysis pipeline includes:

- Text preprocessing
- Tokenization
- Stop-word removal
- Lemmatization
- Transformer-based sentiment classification

The pipeline was implemented using:

- transformers
- spaCy
- NLTK
- pandas

---

## Sentiment Aggregation

Sentiment was aggregated:

- By bank
- By star rating

This helped measure customer satisfaction trends across applications and ratings.

### Example Analysis

- 1-star reviews were generally associated with negative sentiment.
- 5-star reviews showed highly positive sentiment scores.
- Bank sentiment comparisons helped identify stronger and weaker customer experiences.

---

# Thematic Analysis

## Objective

Thematic analysis was performed to identify recurring business-related issues and customer needs from review text.

---

## Theme Categories

The following themes were identified from customer reviews:

| Theme | Description |
|---|---|
| Account Access Issues | Login problems, OTP issues, password failures |
| Transaction Performance | Slow transfers, failed transactions, payment delays |
| UI & UX | Ease of use, interface quality, navigation |
| Customer Support | Support responsiveness and service quality |
| Feature Requests | Requests for new features and app improvements |
| Positive Experience | Positive feedback about usability and performance |

---

## Keyword Extraction

TF-IDF (Term Frequency–Inverse Document Frequency) was used to extract important keywords and phrases from reviews.

Both:

- Unigrams (single words)
- Bigrams (two-word phrases / n-grams)

were analyzed.

### Example Keywords and N-grams

- login error
- slow transfer
- failed payment
- fingerprint login
- good app

---

## Theme Grouping Logic

Themes were created by grouping semantically related keywords extracted using TF-IDF and domain knowledge of fintech mobile applications.

Examples:

- Keywords such as "login", "password", and "otp" were grouped into "Account Access Issues".
- Terms like "transfer", "slow", and "payment failed" were grouped into "Transaction Performance".
- Words related to usability and navigation were grouped into "UI & UX".

---

# NLP Preprocessing Pipeline

A modular NLP preprocessing pipeline was implemented using spaCy and NLTK.

The preprocessing workflow includes:

- Tokenization
- Stop-word removal
- Optional lemmatization
- Text normalization

This preprocessing improves:

- Sentiment accuracy
- Theme detection
- Keyword consistency
- Overall text quality

---

# Output Dataset

The processed analysis dataset contains the following columns:

- review_id
- review_text
- sentiment_label
- sentiment_score
- identified_theme

The final processed dataset was exported as a CSV file for downstream analysis and visualization.

---

# Visualization and Analysis

Several visualizations were created to support business insights, including:

- Sentiment distribution by bank
- Average sentiment by rating
- Theme frequency analysis
- Keyword frequency charts

These visualizations help identify:

- Customer pain points
- Satisfaction drivers
- Common complaints
- Product improvement opportunities

---

# Key Findings

## Common Customer Pain Points

- Slow transaction processing
- Login and OTP issues
- Frequent update requests
- App crashes and loading delays

## Common Satisfaction Drivers

- Easy navigation
- Fast transfers
- Secure mobile banking experience
- User-friendly interface

---

# Running Sentiment and Theme Analysis

## Run Analysis Pipeline

```bash
python scripts/run_analysis.py
```

---

# Libraries Used

- transformers
- torch
- scikit-learn
- spaCy
- NLTK
- pandas
- matplotlib
- seaborn

---

# Task 2 Deliverables

The following deliverables were completed:

- Transformer-based sentiment analysis
- Sentiment aggregation by bank and rating
- TF-IDF keyword extraction
- N-gram analysis
- Theme classification
- Modular NLP preprocessing pipeline
- Exported processed dataset
- Visualization scripts

---

# Conclusion

Task 2 was completed successfully.

Customer reviews were analyzed using transformer-based NLP techniques to uncover customer sentiment and recurring themes across Ethiopian banking applications.

The analysis identified major pain points such as transaction delays, login issues, and update frustrations, while also highlighting positive customer experiences related to usability and app performance.

The processed dataset and insights are ready for:

- PostgreSQL database storage
- Advanced visualization
- Business recommendation generation
- Customer experience analytics

# Author

Lalise Fufi

10 Academy — Artificial Intelligence Mastery Program