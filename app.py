from cgitb import html
from flask import Flask, request
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
from dataparser import Parser

    

provinces = {}

parser = Parser

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    global provinces
    if request.method == "POST":
        url = request.form.get('url')
        prv = request.form.get('prov')
        res = f'Received {prv} data from {url}...'
        data_html = request.form.get('data_html')
        print(res)
        
        if prv not in provinces.keys():
            provinces[prv] = {}
        
       
        if 'throne' in url:
            data_html = request.form.get('data_html')
            provinces[prv].update(parser.throne(data_html))
            print(provinces[prv])
    
        if 'build' in url:
            data_html = request.form.get('data_html')
            provinces[prv].update(parser.build(data_html))
            print(provinces[prv])
            
      
        return provinces[prv]

    if request.method == 'GET':
        return provinces


if __name__ == "__main__":
    app.run()

