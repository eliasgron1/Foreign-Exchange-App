import requests
import utils, defs
import pandas as pd

# Wrapping the oanda api into a class so we can make useful functions for handling the api requests
# making the process look nice and easier to use


class OandaAPI():
    
    def __init__(self):
        self.session = requests.Session()


        # INSTRUMENTS

    def fetch_instruments(self):
        url = f"{defs.OANDA_URL}accounts/{defs.ACCOUNT_ID}/instruments"
        response = self.session.get(url, params=None, headers=defs.SECURE_HEADER)
        return response.status_code, response.json()

    def get_instruments_df(self):
        status, data = self.fetch_instruments()
        if(status==200):
            dataframe = pd.DataFrame.from_dict(data['instruments'])
            return dataframe[['name','type','displayName', 'pipLocation', 'marginRate']]
        else: return None

    def save_instruments(self):
        dataframe = self.get_instruments_df()
        if(dataframe is not None):
            dataframe.to_pickle(utils.get_instruments_data_filename())
        else: return 1


        # CANDLES

    def fetch_candles(self, name, count, gran):
        url = f"{defs.OANDA_URL}/instruments/{name}/candles"
        params = dict(
            count = count,
            granularity = gran,
            price = "MBA"
        )
        response = self.session.get(url, params=params, headers=defs.SECURE_HEADER)
        return response.status_code, response.json()
    
    def get_candles_df(self, json_data):
        prices = ['mid', 'bid', 'ask']
        ohlc = ['o','h','l','c']

        data = []
        for candle in json_data['candles']:
            if candle['complete'] == True:
                new_dict = {}
                new_dict['time'] = candle['time']
                new_dict['volume'] = candle['volume']
                for price in prices:
                    for item in ohlc:
                        new_dict[f"{price}_{item}"] = candle[price][item]

                data.append(new_dict)
        return pd.DataFrame.from_dict(data)
    
    def save_candles(self, dataframe, pair):
        if(dataframe is not None):
            dataframe.to_pickle(utils.get_historic_candles_filename(pair))
            #print(f"Saved:{pair}")
        else: return 1

        
if(__name__ == "__main__"):
    api = OandaAPI()