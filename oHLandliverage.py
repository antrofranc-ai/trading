#!/usr/bin/env python3

import requests
import texttable as tt
from bs4 import BeautifulSoup
tab = tt.Texttable()
tab.set_deco(tab.HEADER)
tab.set_cols_align(["l", "c", "c", "c", "c"])
tab.set_cols_dtype(['t',  # text
                    'f',  # float (decimal)
                    't',  # text
                    't',  # text
                    'f']) # float (decimal)
res = requests.get('https://docs.google.com/spreadsheets/d/1rBV78LxZcu2J2L5rCEaBPAujnY4NJEbxLMqsfQXxh0g/pubhtml/sheet?headers=false&gid=0').text
res2 = requests.get('https://zerodha.com/margin-calculator/Equity/').text
soup = BeautifulSoup(res, 'html.parser')
soup2= BeautifulSoup(res2, 'html.parser')
headings = [soup.tbody.tr.contents[j].text for j in {1,7,9,5}]
headings.append('ZERODHA')
tab.add_row(headings)
for i in soup.tbody.contents:
    if i.contents[9].text == 'OPEN=HIGH' or i.contents[9].text == 'OPEN=LOW':
        contents = [i.contents[j].text for j in {1,7,9,5}]
        stock=contents[0]
        st=stock+':EQ'
        for row in soup2.tbody.findAll('tr'):
            for td in row.findAll('td'):
                if td.text == st:
                    contents.append(td.findNext(attrs='mis').text.strip())
                    tab.add_row(contents)
print(tab.draw())
