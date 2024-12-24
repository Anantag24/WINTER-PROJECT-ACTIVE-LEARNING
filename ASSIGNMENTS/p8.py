import pandas as pd

data = {
    "Product": ["Apple", "Banana", "Cherry", "Date", "Eggfruit", "Fig", "Grape", "Honeydew"],
    "Price": [50, 20, 100, 150, 80, 120, 70, 90],
    "Quantity": [10, 15, 5, 8, 7, 6, 12, 4]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df["Total Value"] = df["Price"] * df["Quantity"]

df_sorted = df.sort_values(by="Total Value", ascending=False)

print("DataFrame Sorted by Total Value:")
print(df_sorted)