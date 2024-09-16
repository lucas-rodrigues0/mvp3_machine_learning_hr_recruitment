import pandas as pd


class Loader:

    def load_data(url:str, attributes: list):

        return pd.read_csv(url, names=attributes, header=0, skiprows=0, delimiter=',')
