import pandas as pd

from project_structure.pipeline.transform import concat_dataframes

df1 = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
df2 = pd.DataFrame({'col1': [4, 5, 6], 'col2': ['d', 'e', 'f']})


def test_dataframe_list_concatenation_test():
    arrange = pd.concat([df1, df2], ignore_index=True)
    act = concat_dataframes([df1, df2])

    assert act.equals(arrange)
