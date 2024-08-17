import pandas as pd
from typing import List

def concat_dataframes(dataframe_list: List[pd.DataFrame]):
    """Function created to concatenate the entire list of dataframes into one dataframe"""
    return pd.concat(dataframe_list, ignore_index=True)
