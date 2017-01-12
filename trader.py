import logging
import argparse
import sys
import tickers
import glob
import os
import config
import time
import inspect
from tickers.bitfinexUSD import BitfinexUSD
from lib import settings

class ExampleTrader(object):

    def __init__(self):
        self.markets = []


    def tick(self):
        pass


    def tickers(self):
        pass

    def update_orderbooks(self):
        """
            This will basically update the orderbooks or
            depths of the markets being spawned
        :return:
        """
        pass

    def loop(self):
        try:
            while True:
                self.depths = self.update_orderbooks()
                self.tickers()
                self.tick()
                time.sleep(config.refresh_rate)

        except KeyboardInterrupt:
            print("\nExit\n")
            exit()