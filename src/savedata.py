import requests
import defs, utils
import oanda_api
import pandas as pd

# This script saves candles to the /data folder as .pkl files

CANDLE_AMOUNT = 5000
GRANULARITY = "H1"

session = requests.Session()

ins_df = pd.read_pickle(utils.get_instruments_data_filename())

api = oanda_api.OandaAPI()

def save_data():
    print(utils.get_currency_pairs())

    for pair in utils.get_currency_pairs():

        status_code, json = api.fetch_candles(pair, CANDLE_AMOUNT, GRANULARITY)
        dataframe = api.get_candles_df(json)
        api.save_candles(dataframe, pair)
        
        print(f"status:{status_code}, pair:{pair}")
         
 