import pandas as pd

# Customer data
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai']
})

# Order data
orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104, 105],
    'CustomerID': [1, 2, 2, 5, 3],
    'Amount': [250, 150, 400, 120, 300]
})

print("Customers:\n", customers, "\n")
print("Orders:\n", orders)


# merge

merged_inner=pd.merge(customers,orders,on='CustomerID',how='inner')
print(f'Inner Merge:\n{merged_inner}')

merged_left=pd.merge(customers,orders,on='CustomerID',how='left')
print(f'Left Merge\n{merged_left}')

merged_right=pd.merge(customers,orders,on='CustomerID',how='right')
print(f'Right Merge\n{merged_right}')

merged_outer=pd.merge(customers,orders,on='CustomerID',how='outer')
print(f'Outer Merge\n{merged_outer}')