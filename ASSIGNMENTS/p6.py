import numpy as np

array_3d = np.random.rand(3, 4, 5)
print("3D Array:")
print(array_3d)

mean_value = np.mean(array_3d)
median_value = np.median(array_3d)
std_dev_value = np.std(array_3d)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev_value}")

normalized_array = (array_3d - mean_value) / std_dev_value
print("Normalized Array:")
print(normalized_array)