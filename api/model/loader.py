import pandas as pd


class Loader:
    """Load a dataset in a pandas dataframe."""

    def load_data(url: str, attributes: list):

        return pd.read_csv(url, names=attributes, header=0, skiprows=0, delimiter=",")
