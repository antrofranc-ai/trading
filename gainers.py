#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from tabulate import tabulate
options = Options()
options.set_headless(headless=True)

driver = webdriver.Firefox(firefox_options=options)
driver.get('https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm')
data = driver.page_source
driver.close()
soup_nse_topgainer = BeautifulSoup(data, "html.parser")
list_ganiners=[]
for tr in soup_nse_topgainer.find_all('tr'):
    for stock in tr.find_all('a'):
        list_ganiners.append(stock.text)
for stocks in list_ganiners:
    print(stocks)
