# import site

# print(site.getsitepackages())

# import sys

# for path in sys.path:
#     print(path)
"""Main module of the ETL process."""

from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_dataframes

if __name__ == '__main__':
    input_path = 'data/input'
    output_path = 'data/output'
    dataframe_list = extract_from_excel(input_path)
    concatenated_dataframe = concat_dataframes(dataframe_list)
    load_excel(concatenated_dataframe, output_path, 'concatenated_excel')
    print(f'Process finished. Check {output_path}')
