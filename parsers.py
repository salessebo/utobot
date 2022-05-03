from bs4 import BeautifulSoup
import pandas as pd

def parse_throne(html_data):
    table_data = pd.read_html(html_data)
    print(table_data)
    return table_data

