import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/pandas_test_dataset.csv')

df['Revenue']=df['Quantity']*df['UnitPrice']


# Exercise 1: Pivot Table Basics
pivot=df.pivot_table(
    values='Revenue',
    index='City',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)
print(pivot)

# Exercise 2: Pivot Table with Multiple Metrics
pivot_multi=df.pivot_table(
    values=['Revenue','Quantity'],
    index='City',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)
print(pivot_multi)

# Exercise 3: Aggregate by Customer
pivot_cust=df.groupby('Customer').agg({
    'Revenue':['sum'],
    'Quantity':['sum']
})
print(pivot_cust)


# Exercise 4: Filter after Aggregation
# Customers with total Revenue > 30000

high_val_cust=pivot_cust[pivot_cust[('Revenue','sum')]>30000]
print(high_val_cust)

# Products with total Quantity sold > 3

agg_product=df.groupby('Product').agg({'Quantity':'sum'})
popular_products=agg_product[agg_product['Quantity']>3]

print(popular_products)

# Exercise 5: Customer × Product Pivot

pivot_3=df.pivot_table(
    values='Revenue',
    index='Customer',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)

print(pivot_3)

# Highest Revenue combination

max_revenue=pivot_3.stack().idxmax()

print(max_revenue)

df.groupby('Product')['Revenue'].sum().plot(kind='bar', title='Revenue by Product')
