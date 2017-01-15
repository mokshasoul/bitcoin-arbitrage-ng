import requests
import json
from lib.export import csvexport
from lib.settings import btfnx_api_url as marketuri
from lib.settings import btfnx_cur_symbol as marketsymbol
from lib.csv_writer import  output_csv_bitfenix
from .market import Market

class BitfinexUSD(Market):

    def __init__(self,currency, marketuri):
        super().__init__("USD", marketsymbol["USD"])
        self.update_rate = 20


    def update_depth(self):
        orderbook_json = self.request_orderbook()
        orderbook_list_dict = self.dictionarize_orderbook(orderbook_json)
        csvexport(orderbook_json)
        # output_csv_bitfenix('asks', r.text)
        # output_csv_bitfenix('bids', r.text)
        return orderbook_list_dict


    def dictionarize_orderbook(self, orderbook_json):
        orderbook_list_dict = []
        return orderbook_list_dict
