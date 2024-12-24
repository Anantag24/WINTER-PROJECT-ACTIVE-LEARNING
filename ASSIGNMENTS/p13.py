import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
months = np.arange(1, 15) 
revenue = np.random.randint(1000, 5000, size=14)

plt.plot(months, revenue, label='Monthly Revenue', color='r', marker='.')

plt.title("company monthly revenue")
plt.xlabel("month")
plt.ylabel('Revenue ($)') 
plt.legend() 

plt.grid(True)
plt.show()