from flask import Flask, request, render_template
from exa_py import Exa
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
exa = Exa(api_key=os.getenv("EXA_API_KEY"))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        response = exa.search(
            query,
            num_results=5,
            type='keyword',
            include_domains=['https://www.reddit.com'],
        )
        results = response.results
    else:
        query = None
        results = []
    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)





