import json
import csv
import datetime
import os


def output_csv_bitfenix(csv_type, parsed_json):
    filename = "bitfenix_" + csv_type + "_" +\
               datetime.datetime.now().strftime("%Y_%M_%D")
    file_exists = os.path.isfile(filename)
    dict_keys = parsed_json[csv_type][0]
    with open(filename, 'a') as f:
        w = csv.DictWriter(f, dict_keys.keys())
        if not file_exists:
            w.writeheader()
        for y in parsed_json[csv_type]:
            y['timestamp'] = datetime.datetime.fromtimestamp(float(y['timestamp'])).strftime("%H:%M:%S %Y-%m-%d")
            w.writerow(y)


def output_csv_kraken(csv_type, parsed_json):
    pass
