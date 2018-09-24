#!/usr/bin/env python3

import json,requests
import pandas as pd
url_nifty_indexes = 'https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/liveIndexWatchData.json'
resp_nifty_indexes = requests.get(url_nifty_indexes)
data_nifty_indexes = json.loads(resp_nifty_indexes.text)
dict_nifty_indexes = {}
indexes = ['NIFTY BANK', 'NIFTY FIN SERVICE', 'NIFTY FMCG', 'NIFTY PSU BANK', 'NIFTY AUTO', 'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PVT BANK', 'NIFTY REALTY']
for index in  data_nifty_indexes['data']:
    if index['indexName'] == 'NIFTY 50':
        print("{}\t{}".format(index['indexName'], index['percChange']))
    if index['indexName'] in indexes:
        if index['indexName'] == 'NIFTY FIN SERVICE':
            dict_nifty_indexes['NIFTY FIN SRV'] = index['percChange']
        else:
            dict_nifty_indexes[index['indexName']] = index['percChange']
sorted_dict_nifty_indexes = OrderedDict(sorted(dict_nifty_indexes.items(), key=lambda x:x[1], reverse=True))
print("="*10)
print("{}\t\t{}".format('INDEX','PERCENTAGE'))
print("-"*10)
for index, percentages in sorted_dict_nifty_indexes.items():
    print("{}\t{}".format(index, percentages))
