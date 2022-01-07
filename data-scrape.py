# # Load libraries
# import urllib.request
# import time
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd
# from urllib.request import urlopen

x = 1
print(x)

url = 'https://en.wikipedia.org/wiki/2016_Formula_One_World_Championship#Season_calendar'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')
tables.type()