#!/usr/bin/env python3

Usage = """./liverage STOCK_NAME"""

def margin(stock):
    st=stock+':EQ'
    #print(st)
    for row in soup.tbody.findAll('tr'):
        for td in row.findAll('td'):
            if td.text == st:
                print(td.text)
                print(td.findNext(attrs='mis').text.strip())
if __name__ == "__main__":
	import requests
	import sys
	from bs4 import BeautifulSoup
	res = requests.get('https://zerodha.com/margin-calculator/Equity/').text
	soup = BeautifulSoup(res, 'html.parser')
	#try:
	stock = sys.argv[1]
	#except IndexError:
	#	print(Usage)		
	#print(sys.argv[1])
	margin(stock)
