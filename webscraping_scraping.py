# -*- coding: utf-8 -*-
"""Webscraping_Scraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zuWqOTr8iKgJI0k6dZguWnc4RsKqx77P
"""

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Identify the URL
URL = "https://standardebooks.org/ebooks"

page = requests.get(URL)
page.status_code

# Extracting the HTML code of the Webpage
htmlcode = page.text
soup = BeautifulSoup(htmlcode)
htmlcode

content = soup.find("ol", attrs={'class' : 'ebooks-list grid'})
text=content.text
# print(text)

r1 = text.split("\n")
# print(r1)

r2 = []
for i in r1:
  if i != '' and i !='\r':
    r2.append(i)
# print(r2)

r3 = []
for i in r2:
  k = i.strip()
  r3.append(k)
# print(r3)

r4 = []
for i in r3:
  if i !='':
    r4.append(i)
# print(r4)

Book_name=[]
Author_name=[]
for i in range(0,len(r4),2):
  Book_name.append(r4[i])
  Author_name.append(r4[i+1])
print(Book_name)
print(Author_name)

df = pd.DataFrame({'Book_Name':Book_name , 'Author_Name': Author_name})
print(df)

df.to_csv("products.csv", header=True, index=False)