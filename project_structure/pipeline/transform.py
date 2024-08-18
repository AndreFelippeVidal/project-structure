from typing import List

import pandas as pd


def concat_dataframes(dataframe_list: List[pd.DataFrame]):
    """Function created to concatenate the entire list of dataframes into one dataframe"""
    print(f"Concatenating files.")
    return pd.concat(dataframe_list, ignore_index=True)
