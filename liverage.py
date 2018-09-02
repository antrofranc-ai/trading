#!/usr/bin/env python3

Usage = """./liverage STOCK_NAME"""

def margin(stock, stock_price):
	st=stock+':EQ'
	#print(st)
	for row in soup.tbody.findAll('tr'):
		for td in row.findAll('td'):
			if td.text == st.upper():
				print(td.text)
                		#print(td.findNext(attrs='mis').text.strip())
				liverage=int(td.findNext(attrs='mis').text.strip().strip('x'))
				print(liverage)
				amount=31000
				print(amount)
				number_of_stocks=(amount*liverage)/stock_price
				print(number_of_stocks)
if __name__ == "__main__":
	import requests
	import sys
	from bs4 import BeautifulSoup
	res = requests.get('https://zerodha.com/margin-calculator/Equity/').text
	soup = BeautifulSoup(res, 'html.parser')
	stock = sys.argv[1]
	stock_price = float(sys.argv[2])
	#print(sys.argv[1])
	margin(stock, stock_price)
