from os import link
from time import daylight
from bs4 import BeautifulSoup
import requests
from fastnumbers import isfloat 
from fastnumbers import fast_float
import pandas as pd
import time 
t=time.asctime( time.localtime(time.time()) )
print(t[:10])