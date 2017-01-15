#/usr/bin/python3

import time
import requests
import logging
import sys
import traceback


class Market(object):
    def __init__(self, currency, symbol,
                 marketuri):
        """

        :param symbol: Symbol indicates which two currency pairs
        are polled when updating the orderbook
        """
        v
        self.currency = currency
        self.symbol =  symbol
        self.marketuri = marketuri

    def request_orderbook(self):
        """
            Will use the update_depth to
        :return: processed dictionary d['asks'] and d['bids']
        """
        book_url = self.marketuri['orderbook'] + self.symbol
        r = requests(book_url)
        return r.json


    # Abstract methods
    def update_depth(self):
        """
            This function polls the orderbook of a Market
            and returns it as a list of dictionaries in
            asks and bids format
        :return:
        """
        pass


    # TODO: Define rules on how the data should be dictionarized
    # that means what has to always be available
    # Abstract methods
    def dictionarize_orderbook(self, orderbook_dic):
        """
        Make a dictionary out of the available input data depending
        on the input provided by a certain market homogeneous
        with price, volume, timestamps
        :return:
        """
        pass


    def sort_and_format(self, l, reverse=False):
        l.sort(key=lambda x: float(x['price']), reverse=reverse)
        r = []
        for i in l:
            r.append({'price': float(i['price']), 'amount': float(i[1])})
        return r


    def format_depth(self, depth):
        bids = self.sort_and_format(depth['result'][self.code]['bids'], True)
        asks = self.sort_and_format(depth['result'][self.code]['asks'], False)
        return {'asks': asks, 'bids': bids}