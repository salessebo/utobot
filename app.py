from cgitb import html
from flask import Flask, request
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
from parser import Parser

    
    
nko = {}

parser = Parser

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    global nko
    if request.method == "POST":
        url = request.form.get('url')
        prv = request.form.get('prov')
        res = f'Received {prv} data from {url}...'
        print(res)
        data_html = request.form.get('data_html')
        print(data_html)
        if 'throne' in url:
            data_html = request.form.get('data_html')
            nko.update(parser.throne(data_html))
            print(nko)
        return nko

    
    if request.method == 'GET':
        return nko


if __name__ == "__main__":
    app.run()

