import numpy as np

array2d = np.random.randint(1, 10, size=(4, 4))  
arrcol = np.random.randint(1, 10, size=(4, 1))
print("2D Array (4x4):")
print(array2d)
print("Column Array (4x1):")
print(arrcol)

result = array2d + arrcol
print("Result of Broadcasting and Addition:")
print(result)