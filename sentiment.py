from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.

    Parameters:
    text (str): The text to analyze.

    Returns:
    str: The sentiment of the text ("Positive", "Negative", or "Neutral").
    """
    if not isinstance(text, str) or text.strip() == "":
        raise ValueError("Input must be a non-empty string.")
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Tests:
test_cases = [
    #Positive sentiments
    "I love this phone!",
    "It's amazing.",
    "I am very happy with the service.",
    "The experience was fantastic.",

    #Negative sentiments
    "I hate this product.",
    "This is the worst experience I've ever had.",
    "I am very disappointed with the quality.",
    "The service was terrible.",

    #Neutral sentiments
    "The product is alright.",
    "The book is on the table.",
    "The meeting starts at 3 PM.",
    "This is a laptop.",

    # Edge cases
    "This movie was sick.",
    "Great, another delay. Just what I needed.",
]

# Run tests
for text in test_cases:
    print(f"{text} -> {analyze_sentiment(text)}")