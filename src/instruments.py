import requests
import utils
import pandas as pd


class Instrument():
    def __init__(self, atr):
        self.name = atr['name'] 
        self.ins_type = atr['type']
        self.displayName = atr['displayName']
        self.pipLocation = pow(10,atr['pipLocation'])
        self.marginRatem = atr['marginRate']

    def __repr__(self):
        return str(vars(self))
    
    @classmethod
    def get_instrument_df(cls):
        return pd.read_pickle(utils.get_instruments_data_filename())
    
    @classmethod
    def get_instrument_list(cls):
        dataframe = cls.get_instrument_df()
        list = dataframe.to_dict(orient='records') 
        return [Instrument(item) for item in list]
 


 
if __name__ == "__main__":
    print(Instrument.get_instrument_list())
