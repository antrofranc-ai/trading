#!/usr/bin/env python3

import json,requests
import pandas as pd
url_gainers_nifty50 = "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
url_gainers_nifty_next50 = "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/jrNiftyGainers1.json"
url_fno_gainers = "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/fnoGainers1.json"
url_losers_nifty50 = "https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json"
url_losers_nifty_next50 = "https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/jrNiftyLosers1.json"
url_fno_losers = "https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/fnoLosers1.json"
url_volume_gainers = "https://www.nseindia.com/live_market/dynaContent/live_analysis/volume_spurts/volume_spurts.json"
url_oi_spurts = "https://www.nseindia.com/live_market/dynaContent/live_analysis/oi_spurts/topPositiveOIChangeData.json"
resp_gainers_nifty50 = requests.get(url_gainers_nifty50)
data_gainers_nifty50 = json.loads(resp_gainers_nifty50.text)
resp_gainers_nifty_next50 = requests.get(url_gainers_nifty_next50)
data_gainers_nifty_next50 = json.loads(resp_gainers_nifty_next50.text)
resp_fno_gainers = requests.get(url_fno_gainers)
data_fno_gainers = json.loads(resp_fno_gainers.text)
resp_losers_nifty50 = requests.get(url_losers_nifty50)
data_losers_nifty50 = json.loads(resp_losers_nifty50.text)
resp_losers_nifty_next50 = requests.get(url_losers_nifty_next50)
data_losers_nifty_next50 = json.loads(resp_losers_nifty_next50.text)
resp_fno_losers = requests.get(url_fno_losers)
data_fno_losers = json.loads(resp_fno_losers.text)
resp_volume_gainers = requests.get(url_volume_gainers)
data_volume_gainers = json.loads(resp_volume_gainers.text)
resp_oi_spurts = requests.get(url_oi_spurts)
data_oi_spurts = json.loads(resp_oi_spurts.text)
gainers_nifty50=[] 
for stock in data_gainers_nifty50['data']:
    gainers_nifty50.append(stock['symbol'])
gainers_nifty_next50=[]
for stock in data_gainers_nifty_next50['data']:
    gainers_nifty_next50.append(stock['symbol'])
fno_gainers=[]
for stock in data_fno_gainers['data']:
    fno_gainers.append(stock['symbol'])
fno_losers=[] 
for stock in data_fno_losers['data']:
    fno_losers.append(stock['symbol'])
losers_nifty50=[] 
for stock in data_losers_nifty50['data']:
    losers_nifty50.append(stock['symbol'])
losers_nifty_next50=[]
for stock in data_losers_nifty_next50['data']:
    losers_nifty_next50.append(stock['symbol'])
volume_gainers=[] 
for stock in data_volume_gainers['data']:
    volume_gainers.append(stock['sym'])
oi_spurts=[] 
for stock in data_oi_spurts['data']:
    oi_spurts.append(stock['symbol'])
gainers = gainers_nifty50 + gainers_nifty_next50
losers = losers_nifty50 + losers_nifty_next50
gainers_losers = gainers + losers
fno_gainers_fno_losers = fno_gainers + fno_losers
#set_1, set_2, set_3, set_4 = set(gainers_losers), set(fno_gainers_fno_losers), set(volume_gainers), set(oi_spurts)
#common_cash_fno_vol_oi = list(set_1 & set_2 & set_3 & set_4)
#set_11, set_22, set_33 = set(gainers_losers), set(fno_gainers_fno_losers), set(volume_gainers)
#common_cash_fno_vol = list(set_11 & set_22 & set_33)
common_vol_oi = list(set(volume_gainers).intersection(oi_spurts))
common_cash_fno = list(set(gainers_losers).intersection(fno_gainers_fno_losers))
common_cash_fno_vol_oi = list(set(common_vol_oi).intersection(common_cash_fno))
common_cash_fno_oi = list(set(common_cash_fno).intersection(oi_spurts))
common_cash_fno_vol = list(set(common_cash_fno).intersection(volume_gainers))
common_cash_volume_gainers = list(set(gainers_losers).intersection(volume_gainers))
common_cash_oi_spurts = list(set(gainers_losers).intersection(oi_spurts))
common_fno_gainers_fno_losers_vol = list(set(fno_gainers_fno_losers).intersection(volume_gainers))
common_fno_gainers_fno_losers_oi = list(set(fno_gainers_fno_losers).intersection(oi_spurts))
common_gainers_fno_gainers = list(set(gainers).intersection(fno_gainers))
common_losers_fno_losers = list(set(losers).intersection(fno_losers))
#print("CASH & FnO & VOL & OI")
#print("{}".format("=" * 6))
#for stock in common_cash_fno_vol_oi:
#    print(stock)
#print("\n----------\n")
#print("CASH & FnO & VOL")
#print("{}".format("=" * 6))
#for stock in common_cash_fno_vol:
#    print(stock)
#print("\n----------\n")
#print("CASH & FnO & OI")
#print("{}".format("=" * 6))
#for stock in common_cash_fno_oi:
#    print(stock)
#print("\n----------\n")
#print("CASH & VOL")
#print("{}".format("=" * 6)) 
#for stock in common_cash_volume_gainers:
#    print(stock)
#print("\n----------\n")
#print("CASH & OI")
#print("{}".format("=" * 6))
#for stock in common_cash_oi_spurts:
#    print(stock)
print("\n----------\n")
print("FnO & VOL")
print("{}".format("=" * 6))
for stock in common_fno_gainers_fno_losers_vol:
    print(stock)
print("\n----------\n")
#print("FnO & IO")
#print("{}".format("=" * 6))
#for stock in common_fno_gainers_fno_losers_oi:
#    print(stock)
#print("\n----------\n")
#print("VOL & OI")
#print("{}".format("=" * 6))
#for stock in common_vol_oi:
#    print(stock)
#print("\n----------\n")
#print("CASH & FnO")
#print("{}".format("=" * 6))
#for stock in common_cash_fno:
#    print(stock)
#print("\n----------\n")
#print("GAINERS-CASH & FnO")
#print("{}".format("=" * 6))
#for stock in common_gainers_fno_gainers:
#    print(stock)
#print("\n----------\n")
#print("LOSERS-CASH & FnO")
#print("{}".format("=" * 6))
#for stock in common_losers_fno_losers:
#    print(stock)
#print("\n----------\n")
#pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df = pd.DataFrame([common_cash_fno_vol_oi, common_cash_fno_vol, common_cash_fno_oi, common_cash_volume_gainers, common_cash_oi_spurts, common_fno_gainers_fno_losers_oi, common_vol_oi, common_cash_fno, common_gainers_fno_gainers, common_losers_fno_losers]).transpose()
df.columns = ["CASH-FnO-VOL-OI |", "CASH-FnO-VOL |", "CASH-FnO-OI |", "CASH-VOL |", "CASH-OI |", "FnO-IO |","VOL & OI", "CASH-FnO |", "G-CASH-FnO", "L-CASH-FnO"]
df=df.fillna(value='')
print(df)
