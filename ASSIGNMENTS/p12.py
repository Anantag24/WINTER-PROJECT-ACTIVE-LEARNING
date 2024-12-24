import pandas as pd

data1 = {'ID': [1, 2, 3, 4, 5],
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']}
df1 = pd.DataFrame(data1)

data2 = {'ID': [1, 2, 3, 4, 6],
'Score': [88, 92, 85, 78, 95]}
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on='ID', how='inner')

print(merged_df)