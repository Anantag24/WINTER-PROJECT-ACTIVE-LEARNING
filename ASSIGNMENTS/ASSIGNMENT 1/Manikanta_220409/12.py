import numpy as np
import pandas as pd

df1 = pd.DataFrame({"ID": [1, 2, 3, 4], "Name": ["Mani", "Hary", "Saga", "Vank"]})
df2 = pd.DataFrame({"ID": [1, 2, 3, 4], "Score": [90, 85, 75, 88]})

merged_df = pd.merge(df1, df2, on="ID")

print(merged_df)

