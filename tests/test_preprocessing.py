import pandas as pd
from src.preprocessing import clean_text

def test_clean_text():

    sample = "This APP is AMAZING!!! https://test.com"

    cleaned = clean_text(sample)

    assert isinstance(cleaned, str)
    assert "http" not in cleaned
    assert "!" not in cleaned