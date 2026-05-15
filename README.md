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
│   └── raw/
│
├── notebooks/
│   ├── __init__.py
│   └── README.md
│
├── scripts/
│   ├── __init__.py
│   ├── scrape_reviews.py
│   └── preprocess_reviews.py
│
├── src/
│   └── __init__.py
│
├── tests/
│   ├── __init__.py
│   └── test_preprocessing.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── fintech_reviews_cleaned.csv
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

# Author

Lalise Fufi

10 Academy — Artificial Intelligence Mastery Program