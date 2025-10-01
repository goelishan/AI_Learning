# Data creation & cleaning
#   Generate fake data
#   Handle missing values
#   String operations
# Merging & joining (combine customers, products, and orders)
# GroupBy & aggregations (e.g., revenue per customer, per product, per city)
# Pivot tables (monthly revenue trends, top categories)
# Apply functions (custom profit margins, discounts)
# Time series (monthly sales trends using pd.to_datetime, resample)
# MultiIndex (customer → product hierarchy)
# Visualization (plot, bar/line charts)
# Export (save results to CSV/Excel)

import pandas as pd
import numpy as np

# create data

customers=pd.DataFrame({
    'CustomerID':range(1,6),
    'Name':['Alice','Bob','Charlie','David','Eva'],
    'City':['Delhi','Mumbai','Bangalore','Chennai','Kolkata']
})

products=pd.DataFrame({
    'ProductID':range(101,106),
    'ProductName': ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories'],
    'Price': [60000, 30000, 20000, 5000, 1000]
})

np.random.seed(42)

orders=pd.DataFrame({
    'OrderID':range(1001,1011),
    'CustomerID':np.random.choice(customers['CustomerID'],10),
    'ProductID':np.random.choice(products['ProductID'],10),
    'Quantity':np.random.randint(1,5,10),
    'OrderDate':pd.date_range(start='2025-01-01',periods=10,freq='15D')
})

print(f'Customer:\n{customers}\n')
print(f'Products:\n{products}\n')
print(f'Orders:\n{orders}\n')

orders_customer=pd.merge(orders,customers,on='CustomerID',how='left')
print(f'order+customer:\n{orders_customer}')

orders_full=pd.merge(orders_customer,products,on='ProductID',how='left')
print(f'order+products\n{orders_full}')

# revenue

orders_full['Revenue']=orders_full['Price']*orders_full['Quantity']
print(f'order+products\n{orders_full}')

# revenue per customer

revenue_per_cust=orders_full.groupby('Name')['Revenue'].sum()
print(revenue_per_cust)

revenue_per_product=orders_full.groupby('ProductName')['Revenue'].sum()
print(revenue_per_product)

pivot_city_table=pd.pivot_table(
    orders_full,
    values='Revenue',
    index=['City','Name'],
    columns='Category',
    aggfunc='sum',
    fill_value=0
)

print(f'City pivot table:\n{pivot_city_table}')

pivot_city_table['Total_Revenue']=pivot_city_table.sum(axis=1)
pivot_city_table_sorted=pivot_city_table.sort_values(by='Total_Revenue',ascending=False)

print(pivot_city_table_sorted)

# monthly revenue trend

orders_full['OrderDate']=pd.to_datetime(orders_full['OrderDate'])

order_ts=orders_full.set_index('OrderDate')

monthly_revenue=order_ts['Revenue'].resample('M').sum()

print(monthly_revenue)


# monthly revenue by category

orders_full['OrderDate']=pd.to_datetime(orders_full['OrderDate'])

monthly_revenue_cat=pd.pivot_table(
    orders_full,
    values='Revenue',
    index=orders_full['OrderDate'].dt.to_period('W'),
    columns='Category',
    aggfunc='sum',
    fill_value=0
)

print(monthly_revenue_cat)


# apply dicsounts

discount_dict={
    'Electronics':0.10,
    'Accessories':0.20
}

def calc_discount_revenue(row):
    discount=discount_dict.get(row['Category'],0)
    return row['Revenue']*(1-discount)

orders_full['Discounted_Revenue']=orders_full.apply(calc_discount_revenue,axis=1)

print(orders_full[['OrderID','ProductName','Category','Revenue','Discounted_Revenue']])


# pivot discounted by city

pivot_discounted=pd.pivot_table(
    orders_full,
    values='Discounted_Revenue',
    index='City',
    columns='Category',
    aggfunc='sum',
    fill_value=0   
)

pivot_discounted['TotalDiscountRevenue']=pivot_discounted.sum(axis=1)

print(pivot_discounted)

orders_full.to_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/orders_full_discounted.csv',index=False)

with pd.ExcelWriter('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/pivot_discounted.xlsx') as writer:
    pivot_discounted.to_excel(writer,sheet_name='City_Category_DiscountRevenue')

print('Export to excel completed!')