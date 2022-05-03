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

        html_data = request.form.get('html_data')
        data = parse_throne(html_data)



        with open('data_html.txt', "w") as data_file:
            data_file.write(data)
        with open('data_html.txt', "r") as data_file:
            res2 = data_file.read()
        return res2

    
    if request.method == 'GET':
        with open('data_html.txt', "r") as data_file:
            res2 = data_file.read()
            return res2
        # return 'Receiving end'


if __name__ == "__main__":
    app.run()

