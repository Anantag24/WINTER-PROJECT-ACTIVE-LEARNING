import matplotlib.pyplot as plt
import numpy as np

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
region_1_sales = [250, 300, 450, 500, 350]
region_2_sales = [280, 320, 400, 480, 380]

x = np.arange(len(products))
width = 0.35  

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, region_1_sales, width, label='Region 1', color='b')
bars2 = ax.bar(x + width/2, region_2_sales, width, label='Region 2', color='g')

ax.set_title('Sales Comparison of Products in Two Regions') 
ax.set_xlabel('Products')
ax.set_ylabel('Sales')  
ax.set_xticks(x)
ax.set_xticklabels(products)
ax.legend()

plt.tight_layout() 
plt.show()