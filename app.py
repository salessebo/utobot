from cgitb import html
from flask import Flask, request
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup




def parse_throne(html_data):
    table_data = pd.read_html(html_data)
    print(table_data)
    df1 = table_data[0][[0,1]]
    df2 = table_data[0][[2,3]]
    df2.columns= [0,1]
    throne_data = pd.concat([df1,df2], ignore_index=True).set_index(0)[1]
    
    soup = BeautifulSoup(html_data, 'lxml')
    spells = [x.get_text(strip=True) for x in soup.find_all("p") if x.get_text(strip=True).startswith('Spell')][0].split(':')[1]
    spells = [x.split('(') for x in spells.split(')')][:-1]
    throne_data['Spells'] = {x: y.split()[0] for x,y in spells}
    throne_data['Networth'] = throne_data['Networth'].split()[0].replace(',','')
    throne_data['Building Eff.'] = throne_data['Building Eff.'].replace('%','')
    throne_data['Stealth'] = throne_data['Thieves'].split()[1].replace('%','').replace('(','').replace(')','')
    throne_data['Mana'] =  throne_data['Wizards'].split()[1].replace('%','').replace('(','').replace(')','')
    throne_data['Thieves'] = throne_data['Thieves'].split()[0].replace(',','')
    throne_data['Wizards'] = throne_data['Wizards'].split()[0].replace(',','')
    personalities = {'Hero':'War Hero'}
    throne_data['Personality'] = [personalities[x] for x in personalities if x in throne_data['Ruler']][0]
    honor_ranks = {'Noble': 'Lord', 'Lord':'Lord', 'Baron':'Baron'}
    throne_data['Honor'] = [honor_ranks[x] for x in honor_ranks if x in throne_data['Ruler']][0]
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
        data_html = request.form.get('data_html')
        print(data_html)
        if 'throne' in url:
            data_html = request.form.get('data_html')
            nko.update(parse_throne(data_html))
            print(nko)
        return nko

    
    if request.method == 'GET':
        return nko


if __name__ == "__main__":
    app.run()

