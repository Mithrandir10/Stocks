from os import mkdir
import os
import pandas as pd
import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
import time
df=pd.DataFrame()
i=1
for i in range(1,29):
    temp=read_csv(f'D:/Stocks/Temp/Stocks{i}.csv',index_col=0)
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
path=f'D:/Stocks/Data/{t}'
mkdir(path)
os.chdir(path)
f1=open(f'{t2}.csv',"w",newline="")
df.to_csv(f1)
#for a in df.values:
#    print(a)