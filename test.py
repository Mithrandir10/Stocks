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
from os import mkdir
import os
import pandas as pd
import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
import time
df=pd.DataFrame()
i=1

temp=read_csv(f'D:/Stocks/Temp/Stocks1.csv',index_col=0)
temp=pd.DataFrame(temp)
df=df.append(temp)
df=df.set_index('Company Name')
print(df)
df=df.dropna()
df=df[df.Price!="-"]
df=df[df.High!="-"]
df=df[df.Low!="-"]
df=df[df.Price!=0]
print(df)
t1=time.asctime( time.localtime(time.time()) )
t1=t1[:10]
t2=time.time()
path=f'D:/Stocks/Data/{t1}'
mkdir(path)
os.chdir(path)
f1=open(f'{t2}.csv',"w",newline="")
df.to_csv(f1)