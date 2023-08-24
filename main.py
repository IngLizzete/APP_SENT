from flask import Flask, render_template, request
from app.sentiment_analysis import analyze_sentiment, load_stopwords

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        text = request.form['text']
        stopwords = load_stopwords()
        sentiment = analyze_sentiment(text, stopwords)
    return render_template('index.html', sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)

