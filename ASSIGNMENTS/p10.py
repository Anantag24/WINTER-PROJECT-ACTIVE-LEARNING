import seaborn as sns
import pandas as pd

iris = sns.load_dataset('iris')

grouped = iris.groupby('species')[['petal_length', 'sepal_width']].mean()

print(grouped)