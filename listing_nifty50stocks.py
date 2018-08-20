#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options)
driver.get('https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm')
data_nr7 = driver.page_source
driver.close()
soup_nr7=BeautifulSoup(data_nr7, "html.parser")
list_stocks=[]
for tr in soup_nr7.find_all('tr'):
    for stock in tr.find_all('a'):
        list_stocks.append(stock.text)
for stocks in list_stocks:
    print(stock)
