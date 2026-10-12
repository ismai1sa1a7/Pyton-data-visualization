import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Creating a basic line plot
plt.plot(x, y)
plt.title('Basic Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.title('Customized Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May']
sales_product_a = [50, 60, 70, 65, 80]
sales_product_b = [40, 55, 60, 70, 75]
sales_product_c = [30, 45, 55, 60, 65]

plt.plot(months, sales_product_a, label='Product A', color='blue', marker='o')
plt.plot(months, sales_product_b, label='Product B', color='red', marker='s')
plt.plot(months, sales_product_c, label='Product C', color='green', marker='^')

plt.legend()

plt.title('Monthly Sales of Products')
plt.xlabel('Months')
plt.ylabel('Sales (Units Sold)')

plt.show()



categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values, color='blue')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='pink', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Data Bins')
plt.ylabel('Frequency')
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in dataset
tips = sns.load_dataset('tips')

# Creating a scatter plot
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex')
plt.title('Scatter Plot of Tips vs. Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()