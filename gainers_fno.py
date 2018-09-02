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
driver.find_element_by_link_text('F&O Securities').click()
#select = Select(driver.find_element_by_id('Gfno'))
#select.select_by_visible_text('F&O Securities')
time.sleep(2)
data_fno = driver.page_source
driver.close()
soup_nse_topgainer_fno = BeautifulSoup(data_fno, "html.parser")
list_gainers_fno=[]
for tr in soup_nse_topgainer_fno.find_all('tr'):
    for stock in tr.find_all('a'):
        list_gainers_fno.append(stock.text)
for stocks in list_gainers_fno:
    print(stocks)
