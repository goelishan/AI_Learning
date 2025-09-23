import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/pandas_test_dataset.csv')

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']


# Exercise 1: Bar Chart - Revenue per Product

plt.figure(figsize=(8,5))
df.groupby('Product')['Revenue'].sum().plot(
    kind='bar',
    color='Skyblue',
    title='Revenue by Product',
)
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.show()

# Exercise 2: Pie Chart - Revenue share by City
plt.figure(figsize=(6,6))
df.groupby('City')['Revenue'].sum().plot(
    kind='pie',
    autopct='%1.1f%%',
    title='Revenue by city'
)
plt.ylabel('')
plt.show()

# Exercise 3: Horizontal Bar Chart - Top Customers by Revenue

plt.figure(figsize=(8,5))
df.groupby('Customer')['Revenue'].sum().sort_values().plot(
    kind='barh',
    color='Green',
    title='Top customers by revenue'
)
plt.xlabel('Revenue')
plt.ylabel('Customer')
plt.show()