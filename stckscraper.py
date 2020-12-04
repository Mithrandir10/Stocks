from os import link
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

url="https://www.moneycontrol.com/india/stockpricequote"
page_response = requests.get(url, timeout=240)
page_content = BeautifulSoup(page_response.content, "lxml")
main_table=page_content.find('div',class_='PT15')
main_table=main_table.find('table')
titles=main_table.find_all('a',class_='bl_12')

links2=[]
    
path='D:/Stocks/Temp'
os.chdir(path)

page_links=page_content.find('div',class_='MT2 PA10 brdb4px alph_pagn')
page_links=page_links.find_all('a')

for i in page_links:
    links2.append(i['href'])
print(links2)
k=0
for i in links2:
 k=k+1
 url=f"https://www.moneycontrol.com{i}"
 page_response = requests.get(url, timeout=240)
 page_content = BeautifulSoup(page_response.content, "lxml")
 main_table=page_content.find('div',class_='PT15')
 main_table=main_table.find('table')
 titles=main_table.find_all('a',class_='bl_12')
 links=[] 
 for i in titles:
    links.append(i['href'])
 links=[i for i in links if i]
 print(links)
 def get_scrip(link_list):
    df=pd.DataFrame(columns=['Company Name','Price','High','Low','Pct Increase'])
    print(df)

    j=0
    for i in link_list:
     print(i)
     original_url = i
     key_val_pairs = {}
     j=j+1
     try:
      page_response = requests.get(original_url)
      page_content = BeautifulSoup(page_response.content, "lxml")
      price_tab=page_content.find('div',class_='pcnsb div_live_price_wrap')
      price=price_tab.find('span').text
      heading=page_content.find('div',class_='moneyprice_bx')
      lh52=page_content.find('div',class_='clearfix lowhigh_band week52_lowhigh_wrap')
      low=lh52.find('div',class_='low_high1').text
      high=lh52.find('div',class_='low_high3').text
      cname=heading.find('h1').text
     
      print(low)
      try:
         low=float(low)
         price=float(price)
      except:
         low=0
         price=0
      if float(low)!=0:
        p_inc=abs((float(price)-float(low))/float(low))*100
      elif float(low)==0:
        p_inc=float(price)*100   
      df.loc[j]=[cname]+[price]+[high]+[low]+[float(p_inc)]
     except:
         pass
     
      
       
    print(df)
    f1=open(f"D:/Stocks/Temp/Stocks{k}.csv","w")
    df.to_csv(f1)
    

 get_scrip(links)
