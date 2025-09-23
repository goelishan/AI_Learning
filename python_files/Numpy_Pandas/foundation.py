import numpy as np
import pandas as pd

data = {
    "OrderID": [101, 102, 103, 104, 105, 106],
    "Customer": ["Alice", "Bob", "Charlie", "Alice", "Bob", "David"],
    "Product": ["Watch", "Ring", "Necklace", "Ring", "Watch", "Bracelet"],
    "Quantity": [1, 2, 1, 3, 2, 1],
    "Price": [5000, 12000, 15000, 12000, 5000, 8000],
    "City": ["Delhi", "Mumbai", "Bangalore", "Delhi", "Mumbai", "Chennai"]
}

df=pd.DataFrame(data)

print(df)

# summarise stats
# print(df.describe())

# total revenue
df['Revenue']=df['Quantity']*df['Price']
print(df[['OrderID','Revenue']])

# group by customer
print(df.groupby('Customer')['Revenue'].sum().sort_values(ascending=False))

# group by city
print(df.groupby('City')['Revenue'].sum())

# most sold product
print(df.groupby('Product')['Quantity'].sum().sort_values(ascending=False))

revenues=df['Revenue'].to_numpy()

print(revenues.mean())
print(revenues.std())
print(np.percentile(revenues,90))