#!/usr/bin/env python3

import requests
import texttable as tt
tab = tt.Texttable()
tab.set_deco(tab.HEADER)
tab.set_cols_align(["l", "c", "c","c"])
tab.set_cols_dtype(['t',  # text
                              'f',  # float (decimal)
                              't',  # text
			      'f']) # float (decimal)
from bs4 import BeautifulSoup
res = requests.get('https://docs.google.com/spreadsheets/d/1rBV78LxZcu2J2L5rCEaBPAujnY4NJEbxLMqsfQXxh0g/pubhtml/sheet?headers=false&gid=0').text
soup = BeautifulSoup(res, 'html.parser')
headings = [soup.tbody.tr.contents[j].text for j in {1,7,9,5}]
tab.add_row(headings)
for i in soup.tbody.contents:
    if i.contents[9].text == 'OPEN=HIGH' or i.contents[9].text == 'OPEN=LOW':
        contents = [i.contents[j].text for j in {1,7,9,5}]
        tab.add_row(contents)
print(tab.draw())
