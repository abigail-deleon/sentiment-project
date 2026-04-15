# Sentiment Analysis Mini Project

## Overview
This project implements a sentiment analysis tool using Python and TextBlob.  
The program takes a sentence as input and classifies it as either Positive, Negative, or Neutral.

---

## Features
- Uses TextBlob for sentiment analysis
- Handles invalid inputs (empty or non-string)
- Classifies sentiment into three categories:
  - Positive
  - Negative
  - Neutral
- Includes test cases with different sentiment types
- Demonstrates common model limitations (negation, sarcasm, subtle tone)

---

## Setup and Run

Make sure you have Python 3 installed.

Install required dependencies:

```bash
python3 -m pip install textblob
python3 -m textblob.download_corpora
python3 sentiment.py
