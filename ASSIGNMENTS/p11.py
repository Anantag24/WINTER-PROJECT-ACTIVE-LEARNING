import pandas as pd
import numpy as np

np.random.seed(0)
data = np.random.randint(1, 100, size=(5, 4))
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

df.loc[1, 'A'] = np.nan
df.loc[3, 'B'] = np.nan
df.loc[4, 'C'] = np.nan
df.loc[2, 'D'] = np.nan

print("Original DataFrame with NaN values:")
print(df)

df_filled = df.apply(lambda x: x.fillna(x.mean()), axis=0)

print("DataFrame after replacing NaN values with the column mean:")
print(df_filled)