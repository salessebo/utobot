from cgitb import html
from flask import Flask, request
from datetime import datetime
from bs4 import BeautifulSoup




def parse_throne(html_data):
    # Parse throne table
#     with open("throne_html.txt", "r") as throne_html:
#         html_data = throne_html.read()
    soup = BeautifulSoup(html_data, 'html.parser')
    table_data = pd.read_html(html_data)
    df1 = table_data[1][[0,1]]
    df2 = table_data[1][[2,3]]
    df2.columns= [0,1]
    throne_data = pd.concat([df1,df2], ignore_index=True).set_index(0)[1]
    throne_data['Message'] = [x.get_text() for x in soup.find_all("p", {"class": "advice-message"})]
    spells = [x.get_text(strip=True) for x in soup.find_all("p") if x.get_text(strip=True).startswith('Spell')][0].split(':')[1]
    throne_data['Spells'] = [x.split('(') for x in spells.split(')')][:-1]
    return throne_data.to_dict()

    
    
nko = {}



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    global nko
    if request.method == "POST":
        url = request.form.get('url')
        prv = request.form.get('prov')
        res = f'Received {prv} data from {url}...'
        print(res)
        if 'throne' in url:
            data_html = request.form.get('data_html')
            nko = parse_throne(data_html)
        return nko

    
    if request.method == 'GET':
        return nko


if __name__ == "__main__":
    app.run()

