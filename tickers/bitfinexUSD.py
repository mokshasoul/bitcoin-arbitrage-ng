import requests
import json
from lib.settings import BTFNX_API_URL as url
from lib.csv_writer import  output_csv_bitfenix
from .market import Market

class BitfinexUSD(Market):

    def __init__(self):
        super().__init__("btcusd")
        self.update_rate = 20

    def update_depth(self):
        book_url = url['order_book'] + self.symbol
        r = requests(book_url)
        output_csv_bitfenix('asks', r.text)
        output_csv_bitfenix('bids', r.text)
        return json.loads(r.text)


