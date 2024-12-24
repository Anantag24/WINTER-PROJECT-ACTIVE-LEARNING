import numpy as np

array = np.random.randint(10, 101, size=25)
print("Original Array:")
print(array)
max_value = np.max(array)
min_value = np.min(array)
max_index = np.argmax(array)
min_index = np.argmin(array)

print(f"\nMaximum Value: {max_value} at Index: {max_index}")
print(f"Minimum Value: {min_value} at Index: {min_index}")

array_with_odds_replaced = np.where(array % 2 != 0, -1, array)

print("\nArray after replacing odd numbers with -1:")
print(array_with_odds_replaced)
