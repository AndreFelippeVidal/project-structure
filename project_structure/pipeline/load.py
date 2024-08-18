import os
from typing import List

import pandas as pd


def load_excel(dataframe: pd.DataFrame, output_pah: str, file_name: str) -> str:
    """ Function to sabe dataframe into excel file.
        args:
        dataframe (pd.Dataframe): dataframe to be saved.
        output_path (str): path for the file to be saved.
        file_name (str): name of the file that will be saved.

        return: 'File saved successfuly.' 

    """
    print("Generating concatenated file.")
    if not os.path.exists(output_pah):
        os.makedirs(output_pah) 
    dataframe.to_excel(f"{output_pah}/{file_name}.xlsx", index=False)
    return "File saved successfuly."


if __name__ == "__main__":
    pass
