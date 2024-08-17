import os
import glob

import pandas as pd
from typing import List

path = "data/input"

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Function to extract data from Excel files.

    type: input_folder: str
    """
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    if not all_files:
        raise ValueError("No Excel files found in the specified folder")

    all_data = [pd.read_excel(file) for file in all_files]

    return all_data
    
if __name__ == "__main__":
    df_list = extract_from_excel(path)
    print(df_list)