import pandas as pd

def get_instruments_data_filename():
    return '../data/instruments.pkl'

def get_historic_candles_filename(pair):
    return f"../data/{pair}.pkl"


def get_currencies():
    return [
    'USD',
    'AUD',
    'EUR',
    'GBP',
    ]

def get_currency_pairs():
    ins_df = pd.read_pickle(get_instruments_data_filename())
    currencies = get_currencies()
    valid_pairs = []
    for p1 in currencies:
        for p2 in currencies:
            pair = f"{p1}_{p2}"

            if pair in ins_df.name.unique():
                valid_pairs.append(pair)
    
    return valid_pairs
