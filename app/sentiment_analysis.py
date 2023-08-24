from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

def load_stopwords():
    stopwords_path = os.path.join(os.path.dirname(__file__), '../data/stopwords.txt')
    with open(stopwords_path, 'r') as f:
        stopwords = set(line.strip() for line in f)
    return stopwords

def analyze_sentiment(text, stopwords):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "Positivo 😀🤩😁"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "Negativo 😞😤😡"
    else:
        sentiment = "Neutral 😑🫢🤫"
    
    return sentiment

