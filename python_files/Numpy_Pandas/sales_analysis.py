import pandas as pd

customers=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/customers_031025.csv')
products=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/products_031025.csv')
sales=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/sales_031025.csv')

# merge sales with customers

cust_sales=pd.merge(customers,sales,on='CustID',how='left')
print(cust_sales)

# merge with products
full_report=pd.merge(cust_sales,products,on='ProdID',how='left',indicator=True)
print(full_report)

full_report['SaleAmount']=full_report['Price']*full_report['Quantity']
print(full_report)

# total sale per region
sale_by_region=full_report.groupby('Region')['SaleAmount'].sum()
print(sale_by_region)

# best selling product by revenue
best_products=full_report.groupby('ProductName')['SaleAmount'].sum().sort_values(ascending=False)
print(best_products)

# customers with missing data
missing_cust=full_report[full_report['Name'].isna()]
print(missing_cust)

# Invalid product sold
inv_prod=full_report[full_report['ProductName'].isna()]
print(inv_prod)

# Monthly sales analysis
full_report['SaleDate']=pd.to_datetime(full_report['SaleDate'])
sales_trend=full_report.groupby(full_report['SaleDate'].dt.to_period('M'))['SaleAmount'].sum()
print(sales_trend)

# Top customers
top_customers=full_report.groupby('Name')['SaleAmount'].sum().sort_values(ascending=False)
print(top_customers)

# Category wise revenue
cat_revenue=full_report.groupby('Category')['SaleAmount'].sum()
print(cat_revenue)