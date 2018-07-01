#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from tabulate import tabulate

#WINDOW_SIZE = "1920,1080"

#firefox_options = Options()
#firefox_options.add_argument("--headless")  

options = Options()
options.set_headless(headless=True)

driver = webdriver.Firefox(firefox_options=options)
driver.get('https://www.nseindia.com/live_market/dynaContent/live_watch/pre_open_market/pre_open_market.htm')

select = Select(driver.find_element_by_id('selId'))
select.select_by_visible_text('FO Stocks')
time.sleep(2)
data = driver.page_source
driver.close()

NSE_premarket_soup = BeautifulSoup(data, "html.parser")
import re
import operator
if not NSE_premarket_soup.find(string='NIFTY 50'):
    NSE_premarket_trlist=[]
    for tr in NSE_premarket_soup.find('table', id="preOpenNiftyTab").findAll('tr'):
        NSE_premarket_tdlist=[]
        if ',' in tr.contents[9].text:
            if float(tr.contents[9].text.replace(',','')) < 50000:
                if float(tr.contents[8].text.replace(',','')) > 60:
                    if float(tr.contents[3].text.replace(',','')) < 450:
                        for td in tr:
                            NSE_premarket_tdlist.append(td.text)
                        NSE_premarket_trlist.append(NSE_premarket_tdlist)
    NSE_premarket_trlist = sorted(NSE_premarket_trlist, key=operator.itemgetter(8))
    heading = []
    for th in NSE_premarket_soup.find('table', id="preOpenNiftyTab").findAll('tr')[1]:
        if not th.string == ' ':
            heading.append(th.string)
    heading[8] = 'Value'
    print(tabulate(NSE_premarket_trlist, heading))
