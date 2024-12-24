import pandas as pd

titanic_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(titanic_url)

under_18 = df[df['Age'] < 18]
print("\nPassengers under 18:")
print(under_18) 
