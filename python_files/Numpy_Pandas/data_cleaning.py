import numpy as np
import pandas as pd

df=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/pandas_test_dataset.csv')

# print(df.head())

# # find null values for each column
# print(df.isnull().sum())

# # replace missing quantity by 1
# df['Quantity'].fillna(1,inplace=True)

# # replace missing value in city with unknown
# df['City'].fillna('Unknown',inplace=True)

# df.fillna({'City':'Unknown'},inplace=True)


# print(df.isnull().sum())

# # drop duplicates
# df.drop_duplicates(inplace=True)

# # rename column
# df.rename(columns={'UnitPrice':'Unit_Price','OrderID':'Order_ID'},inplace=True)


# # convert quantity to integer
# df['Quantity']=df['Quantity'].astype(int)

# # convert Unit_price to float

# df['Unit_Price']=df['Unit_Price'].astype(float)

# # create revenue column
# df['Revenue']=df['Quantity']*df['Unit_Price']

# # print frame where quantity > 2
# print(df[df['Quantity']>2])

# # orders from delhi
# print(df[df['City']=='Delhi'])

# # select only city and revenue
# print(df[['City','Revenue']].groupby('City').sum())

# ----------------------------------------------------------------------------------------------------------------------------------

# revenue >20000
df['Revenue']=df['Quantity']*df['UnitPrice']
print(df[df['Revenue']>20000.0])

# quantity>1 and city=delhi
print(df[(df['Quantity']>1) & (df['City']=='Delhi')])

# customer is alice or bob
print(df[(df['Customer']=='Alice') | (df['Customer']=='Bob')])

# revenue in descending order
print(df['Revenue'].sort_values(ascending=False))

# top 3 customers by total revenue
top_customers=df.groupby('Customer')['Revenue'].sum().sort_values(ascending=False).head(3)
print(top_customers)

# rank orders by revenue

df['Revenue_Rank']=df['Revenue'].rank(method='dense',ascending=False)
print(df[['OrderID','Customer','Revenue','Revenue_Rank']])