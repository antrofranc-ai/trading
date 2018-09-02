#!/usr/bin/env python3

import json,requests
url_gainers = "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
url_fno_gainers = "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/fnoGainers1.json"
url_losers = "https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json"
url_fno_losers = "https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/fnoLosers1.json"
url_volume_gainers = "https://www.nseindia.com/live_market/dynaContent/live_analysis/volume_spurts/volume_spurts.json"
url_oi_spurts = "https://www.nseindia.com/live_market/dynaContent/live_analysis/oi_spurts/topPositiveOIChangeData.json"
resp_gainers = requests.get(url_gainers)
data_gainers = json.loads(resp_gainers.text)
resp_fno_gainers = requests.get(url_fno_gainers)
data_fno_gainers = json.loads(resp_fno_gainers.text)
resp_losers = requests.get(url_losers)
data_losers = json.loads(resp_losers.text)
resp_fno_losers = requests.get(url_fno_losers)
data_fno_losers = json.loads(resp_fno_losers.text)
resp_volume_gainers = requests.get(url_volume_gainers)
data_volume_gainers = json.loads(resp_volume_gainers.text)
resp_oi_spurts = requests.get(url_oi_spurts)
data_oi_spurts = json.loads(resp_oi_spurts.text)
gainers=[] 
for stock in data_gainers['data']:
    gainers.append(stock['symbol'])
fno_gainers=[]
for stock in data_fno_gainers['data']:
    fno_gainers.append(stock['symbol'])
fno_losers=[] 
for stock in data_fno_losers['data']:
    fno_losers.append(stock['symbol'])
losers=[] 
for stock in data_losers['data']:
    losers.append(stock['symbol'])
volume_gainers=[] 
for stock in data_volume_gainers['data']:
    volume_gainers.append(stock['sym'])
oi_spurts=[] 
for stock in data_oi_spurts['data']:
    oi_spurts.append(stock['symbol'])
gainers_losers = gainers + losers
fno_gainers_fno_losers = fno_gainers + fno_losers
set_1, set_2, set_3, set_4 = set(gainers_losers), set(fno_gainers_fno_losers), set(volume_gainers), set(oi_spurts)
common_cash_fno_vol_oi = list(set_1 & set_2 & set_3 & set_4)
set_11, set_22, set_33 = set(gainers_losers), set(fno_gainers_fno_losers), set(volume_gainers)
common_cash_fno_vol = list(set_11 & set_22 & set_33)
common_cash_fno = list(set(gainers_losers).intersection(fno_gainers_fno_losers))
common_cash_volume_gainers = list(set(gainers_losers).intersection(volume_gainers))
common_cash_oi_spurts = list(set(gainers_losers).intersection(oi_spurts))
common_fno_gainers_fno_losers_vol = list(set(fno_gainers_fno_losers).intersection(volume_gainers))
common_fno_gainers_fno_losers_oi = list(set(fno_gainers_fno_losers).intersection(oi_spurts))
common_gainers_fno_gainers = list(set(gainers).intersection(fno_gainers))
common_losers_fno_losers = list(set(losers).intersection(fno_losers))
print("CASH & FnO & VOL & OI")
print("{}".format("=" * 6))
for stock in common_cash_fno_vol_oi:
    print(stock)
print("\n----------\n")
print("CASH & FnO & VOL")
for stock in common_cash_fno_vol:
    print(stock)
print("\n----------\n")
print("CASH & FnO")
print("{}".format("=" * 6)) 
for stock in common_cash_fno:
    print(stock)
print("\n----------\n")
print("CASH & VOL")
print("{}".format("=" * 6)) 
for stock in common_cash_volume_gainers:
    print(stock)
print("\n----------\n")
print("CASH & OI")
print("{}".format("=" * 6))
for stock in common_cash_oi_spurts:
    print(stock)
print("\n----------\n")
print("FnO & VOL")
print("{}".format("=" * 6))
for stock in common_fno_gainers_fno_losers_vol:
    print(stock)
print("\n----------\n")
print("FnO & IO")
print("{}".format("=" * 6))
for stock in common_fno_gainers_fno_losers_oi:
    print(stock)
print("\n----------\n")
print("GAINERS-CASH & FnO")
print("{}".format("=" * 6))
for stock in common_gainers_fno_gainers:
    print(stock)
print("\n----------\n")
print("LOSERS-CASH & FnO")
print("{}".format("=" * 6))
for stock in common_losers_fno_losers:
    print(stock)
print("\n----------\n")
