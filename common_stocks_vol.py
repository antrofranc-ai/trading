#!/usr/bin/env python3

import json,requests
url_nif50 = 'https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json'
resp_nif50 = requests.get(url_nif50)
data_nif50 = json.loads(resp_nif50.text)
nif50=[]
for stock in data_nif50['data']:
    nif50.append(stock['symbol'])
url_nif_next50 = 'https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/juniorNiftyStockWatch.json'
resp_nif_next50 = requests.get(url_nif_next50)
data_nif_next50 = json.loads(resp_nif_next50.text)
nif_next50=[]
for stock in data_nif_next50['data']:
    nif_next50.append(stock['symbol'])
stocks = nif_next50 + nif50
url_volume_gainers = "https://www.nseindia.com/live_market/dynaContent/live_analysis/volume_spurts/volume_spurts.json"
resp_volume_gainers = requests.get(url_volume_gainers)
data_volume_gainers = json.loads(resp_volume_gainers.text)
volume_gainers=[] 
for stock in data_volume_gainers['data']:
    volume_gainers.append(stock['sym'])
common_stocks_vol = list(set(stocks).intersection(volume_gainers))
for stock in common_stocks_vol:
    print(stock)
