import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/survey_031025.csv')

print(df)
print(df.isnull().sum())

# drop useless rows
df=df.dropna(how='all')
print(df.isnull().sum())

# ---------------------------fill missing values-----------------------------------------
# mean age 
df['Age']=df['Age'].fillna(df['Age'].mean())

# name/gender with unknown
df[['Name','Gender']]=df[['Name','Gender']].fillna('Unknown')

# missing feedback with 'No feedback'
df['Feedback']=df['Feedback'].fillna('No feedback')

# missing rating with median value
df.replace({'Rating':np.nan},inplace=True)
df['Rating']=pd.to_numeric(df['Rating'],errors='coerce')
df['Rating']=df['Rating'].fillna(df['Rating'].median())

print(df)

# ----------------------------Transform data-------------------------------------------------

df['Feedback']=df['Feedback'].str.lower()

gender_map={'Male':'M','Female':'F','Unknown':'U'}
df['Gender']=df['Gender'].map(gender_map)

print(df)

# -----------------------------Analysis--------------------------------------------------

# Average ratings by gender
avg_rating=df.groupby('Gender')['Rating'].mean()
print(avg_rating)

# most common feedback words
all_words=df['Feedback'].str.cat(sep=' ').split()
word_count=pd.Series(all_words).value_counts()
print(word_count.head(5))

# age distribution
df['AgeGroup']=pd.cut(df['Age'],bins=[0,20,30,40,50],labels=['<20','20-30','30-40','40-50'])
age_dist=df.groupby('AgeGroup')['CustID'].count()
print(age_dist)