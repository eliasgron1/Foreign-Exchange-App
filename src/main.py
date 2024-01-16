import requests
import pandas as pd
import plotly.graph_objects as go

import defs, utils, savedata, oanda_api, instruments

# Fetch fresh data
savedata.save_data()

pair = "EUR_USD"

session = requests.Session()
url = f"{defs.OANDA_URL}accounts/{defs.ACCOUNT_ID}/instruments"
response = session.get(url, params=None, headers=defs.SECURE_HEADER)


df = pd.read_pickle(utils.get_historic_candles_filename(pair))

print("Status check: ", response.status_code)

for pair in utils.get_currency_pairs():
    print(pair, pd.read_pickle(utils.get_historic_candles_filename(pair)))
