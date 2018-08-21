#!/usr/bin/env python3

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys

BUY = sys.argv[1]
SELL = sys.argv[2]
NUMBER_OF_STOCKS = sys.argv[3]

options = Options()
options.set_headless(headless=True)

browser = webdriver.Firefox(firefox_options=options)
browser.get('https://zerodha.com/brokerage-calculator')
change=browser.find_element_by_xpath('//input[contains(@title,"Buy Price")]')
change.clear()
change.send_keys(BUY)
change=browser.find_element_by_xpath('//input[contains(@title,"Sell Price")]')
change.clear()
change.send_keys(SELL)
change=browser.find_element_by_xpath('//input[contains(@title,"Quantity")]')
change.clear()
change.send_keys(NUMBER_OF_STOCKS)
data = browser.page_source
browser.close()
soup_zerodha_brokerage = BeautifulSoup(data, "html.parser")
if float(soup_zerodha_brokerage.find("span", {"class": "six columns profit"}).text) == 0:
    print(soup_zerodha_brokerage.find("span", {"class": "six columns loss"}).text)
else:
    print(soup_zerodha_brokerage.find("span", {"class": "six columns profit"}).text)

