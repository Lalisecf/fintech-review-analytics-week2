from src.thematic_analysis import identify_theme

def test_theme_detection():

    review = "The login and OTP system is failing"

    theme = identify_theme(review)

    assert theme == "Account Access Issues"