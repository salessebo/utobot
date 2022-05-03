from cgitb import html
from flask import Flask, request
from datetime import datetime
from parsers import parse_throne

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        url = request.form.get('url')
        prv = request.form.get('prov')
        res = f'Received {prv} data from {url}...'
        print(res)
        if 'throne' in url:
            html_data = request.form.get('html_data')
            parse_throne(html_data)
            
        return res

    
    if request.method == 'GET':
        return 'Receiving end'


if __name__ == "__main__":
    app.run()

