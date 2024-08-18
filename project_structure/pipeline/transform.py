"""This is the transform module."""

from typing import List

import pandas as pd


def concat_dataframes(dataframe_list: List[pd.DataFrame]):
    """Concatenates the entire list of dataframes into one dataframe."""
    print(f'Concatenating files.')
    return pd.concat(dataframe_list, ignore_index=True)
