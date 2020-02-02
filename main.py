from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

set(stopwords.words('english'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def post_review():
    stop_words = stopwords.words('english')
    input_text= request.form['input_text'].lower()
    
    processed_doc1 = ' '.join([word for word in input_text.split() if word not in stop_words])

    sia = SentimentIntensityAnalyzer()
    ps = sia.polarity_scores(text=input_text)
    result = round((1 + ps['compound'])/2, 2) * 100
    
    return render_template('home.html', final=result, text=input_text)

@app.route('/test')
def test():
    return 'flask is working properly'

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1:5000", threaded=True)
