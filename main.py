
from flask import Flask, render_template
import requests

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=4f74e98927484aa6a0fb15966662b8e3"
    r= requests.get(url).json()
    case= {
        'articles': r['articles']
    }
    return render_template('index.html', cases= case)

if __name__=='__main__':
    app.run(debug=True)