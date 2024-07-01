from flask import Flask, request, jsonify, render_template
import requests
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

NEWS_API_KEY = '36e543e9023f4a64a94894bd1ce8393a'  # Replace with your actual News API key

def fetch_news(topic):
    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])[:10]
        return articles
    else:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news', methods=['GET'])
def get_news():
    topic = request.args.get('topic', 'AI')
    articles = fetch_news(topic)
    return render_template('news.html', articles=articles, topic=topic)

if __name__ == '__main__':
    app.run(debug=True)
