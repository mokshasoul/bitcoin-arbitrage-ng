import requests
import json
import csv
import datetime
from lib.settings import KRN_API_URL
from functools import reduce

def dictionarize_krn(list123):
    asks = []
    bids = []
    for x in list123['asks']:
        asks.append({'price':x[0], 'volume':x[1], 'timestap':datetime.datetime.fromtimestamp(float(x[0])).strftime("%H:%M:%S %Y-%m-%d")})
    for x in list123['bids']:
        bids.append({'price':x[0], 'volume':x[1], 'timestap':datetime.datetime.fromtimestamp(float(x[0])).strftime("%H:%M:%S %Y-%m-%d")})
    return asks, bids


def main():
    orderbook_url_btfx = 'https://api.bitfinex.com/v1/book/'
    symbol_krn = 'XXBTZUSD'
    symbol_btfx='btcusd'
    orderbook_url_krn = KRN_API_URL['order_book']
    orderbook_url_btfx = orderbook_url_btfx + symbol_btfx
    r_krn = requests.get(orderbook_url_krn, params={ 'pair' : symbol_krn})
    r_btfx = requests.get(orderbook_url_btfx)
    x_btfx = json.loads(r_btfx.text)
    x_krn = json.loads(r_krn.text)['result'][symbol_krn]
    x_krn_ask, x_krn_bid = dictionarize_krn(x_krn)
    # x_krn = r_krn.json()
    # columns = map(lambda x: x.keys(), r)
    # columns = reduce(lambda x,y: x+y, columns)
    # columns = list( set( columns ))s
    # print(columns)
    dict_keys_btfx = x_btfx['asks'][0]
    dict_keys_krn = x_krn_ask[0]
    with open('test_btfx_ask.csv', 'w') as f_ask:
        w = csv.DictWriter(f_ask, dict_keys_btfx.keys())
        w.writeheader()
        for y in x_btfx['asks']:
            y['timestamp'] = datetime.datetime.fromtimestamp(float(y['timestamp'])).strftime("%H:%M:%S %Y-%m-%d")
            w.writerow(y)
    f_ask.close()

    with open('test_btfx_bid.csv', 'w') as f_bid:
        w = csv.DictWriter(f_bid, dict_keys_btfx.keys())
        w.writeheader()
        for y in x_btfx['bids']:
            y['timestamp'] = datetime.datetime.fromtimestamp(float(y['timestamp'])).strftime("%H:%M:%S %Y-%m-%d")
            w.writerow(y)
    f_bid.close()

    with open('test_krn_ask.csv', 'w') as f_ask:
        w = csv.DictWriter(f_ask, dict_keys_krn.keys())
        w.writeheader()
        for y in x_krn_ask:
            w.writerow(y)
    f_ask.close()

    with open('test_krn_bid.csv', 'w') as f_bid:
        w = csv.DictWriter(f_bid, dict_keys_krn.keys())
        w.writeheader()
        for y in x_krn_bid:
            w.writerow(y)
    f_bid.close()

main()