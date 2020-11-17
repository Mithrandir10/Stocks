import numpy as np # linear algebra
import pandas as pd # pandas for dataframe based data processing and CSV file I/O
import requests # for http requests
from bs4 import BeautifulSoup # for html parsing and scraping
import bs4
from fastnumbers import isfloat 
from fastnumbers import fast_float
from multiprocessing.dummy import Pool as ThreadPool 

import matplotlib.pyplot as plt
import seaborn as sns
import json
from tidylib import tidy_document # for tidying incorrect html
from IPython.core.display import HTML

sns.set_style('whitegrid')

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def ffloat(string):
    if string is None:
        return np.nan
    if type(string)==float or type(string)==np.float64:
        return string
    if type(string)==int or type(string)==np.int64:
        return string
    return fast_float(string.split(" ")[0].replace(',','').replace('%',''),
                      default=np.nan)

def ffloat_list(string_list):
    return list(map(ffloat,string_list))

def remove_multiple_spaces(string):
    if type(string)==str:
        return ' '.join(string.split())
    return string

def get_table_simple(table,is_table_tag=True):
    elems = table.find_all('tr') if is_table_tag else get_children(table)
    table_data = list()
    for row in elems:
        row_data = list()
        row_elems = get_children(row)
        for elem in row_elems:
            print(elem)
            text = elem.text.strip().replace("\n","")
            text = remove_multiple_spaces(text)
            if len(text)==0:
                continue
            row_data.append(text)
        table_data.append(row_data)
    return table_data
response = requests.get("http://www.example.com/", timeout=240)
response.status_code
response.content


def get_children(html_content):
    return [item for item in html_content.children if type(item)==bs4.element.Tag or len(str(item).replace("\n","").strip())>0]

def get_scrip_info(url):
    original_url = url
    key_val_pairs = {}
    
    page_response = requests.get(url, timeout=240)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    price = ffloat(page_content.find('span',attrs={'span_price_wrap stprh grn_hilight grnclr'}).text)
    name = page_content.find('h1',attrs={'pcstname'}).text

    yearly_high = page_content.find('div',attrs={'low_high3'}).text.strip()
    yearly_low = page_content.find('div',attrs={'low_high1'}).text.strip()
    html_data_content = page_content.find('div', attrs={'id': 'standalone_valuation'})
    volume = ffloat(page_content.find('span',attrs={'class':'txt13_pc volume_data'}).text)


    

    key_val_pairs['price'] = price
    key_val_pairs['volume'] = volume
    key_val_pairs["yearly_low"] = ffloat(yearly_low)
    key_val_pairs["yearly_high"] = ffloat(yearly_high)
    return key_val_pairs

x=get_scrip_info("https://www.moneycontrol.com/india/stockpricequote/finance-leasinghire-purchase/bajajfinance/BAF")
print(x)