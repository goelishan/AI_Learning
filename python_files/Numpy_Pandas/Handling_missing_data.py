import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", None, "Eva"],
    "Age": [25, None, 30, 28, None],
    "Salary": [50000, 60000, None, 45000, 70000]
}

df=pd.DataFrame(data)

# find missing values
print(df)
print(df.isnull())
print(df.isnull().sum())


# drop missing values
df.dropna()
dt1=df.dropna(subset=['Age'])
df.dropna(how='all')
print(df.isnull().sum())
print(dt1.isnull().sum())


# fill missing values
df['Age']=df["Age"].fillna(0)
df['Salary']=df["Salary"].fillna(df["Salary"].mean())
df['Name']=df["Name"].fillna('Unknown')

print(df)


# apply function to a column
df["Age"]=df["Age"].apply(lambda x:x*2 if x>0 else x)
print(df)


# apply function across dataframe
df = df.map(lambda x: str(x).upper() if isinstance(x, str) else x)
print(df)