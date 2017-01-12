import time
import requests
import logging
import sys
import traceback


class Market(object):

    def __init__(self, symbol):
        """

        :param symbol: Symbol indicates which two currency pairs
        are polled when updating the orderbook
        """
        self.name = self.__class__.__name__
        self.symbol = symbol


    def request_orderbook(self):
        """
            Will use the update_depth to
        :return: processed dictionary d['asks'] and d['bids']
        """


    # Abstract methods
    def update_depth(self):
        """
            This function polls the orderbook of a Market
            and returns it as a list of dictionaries in
            asks and bids format
        :return:
        """
        pass


    # Abstract methods
    def dictionarize_orderbook(self, orderbook ):
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