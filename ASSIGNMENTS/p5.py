import numpy as np

matrix = np.random.randint(1, 101, size=(5, 5))
print("5x5 Random Matrix:")
print(matrix)

diagonal_elements = np.diagonal(matrix)
print("Diagonal Elements:")
print(diagonal_elements)

upper_Elements = np.sum(np.triu(matrix, k=1))
print("Sum of elements above the main diagonal elements:")
print(upper_Elements)