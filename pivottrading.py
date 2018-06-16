#!/usr/bin/env python3

from bs4 import BeautifulSoup
from tabulate import tabulate
import re
import bs4
import requests
pivot = requests.get('http://www.pivottrading.co.in/scanner/openHighLowScanner.php?broker=zerodha').text
soup = BeautifulSoup(pivot, 'html.parser')
heading = []
for td in soup.findAll(style="color: white; font-weight: bold;")[1]:
    heading.append(td.string.strip())
headings = [x for x in heading if x]
tr_l=[]
for tr in soup.find_all(style=re.compile("font-family:Georgia;font-weight:bold;font-size:14px;background")):
    td_l=[]
    for td in tr:
        m = re.compile(r'^([0-9]*.[0-9]+)(.*)$')
        result = m.match(td.text)
        if result:
            td_l.append(result.group(1))
        else:
            td_l.append(td.text)
    tr_l.append(td_l)
print(tabulate(tr_l, headings))
