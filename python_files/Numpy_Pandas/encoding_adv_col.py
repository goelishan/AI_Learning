import pandas as pd

employees=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/employees_adv_031025.csv')
department=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/department_adv_031025.csv')

df=pd.merge(employees,department,on='DeptID',how='left')
print(df)


print(df.isna().sum())

# handle missing values in salary column
df['Salary']=df['Salary'].replace(0,pd.NA)
df['Salary']=df['Salary'].fillna(df['Salary'].median())

# Categorical conversion
df['Gender']=df['Gender'].astype('category')
df['DeptName']=df['DeptName'].astype('category')
df['Manager']=df['Manager'].astype('category')

# label encoding
df['DeptCode']=df['DeptName'].cat.codes
df['GenderCode']=df['Gender'].cat.codes

# one-hot encoding for department
df_dummies=pd.get_dummies(df,columns=['DeptName'],prefix='Dept')


# conditional columns
df['Senior']=df['Age'].apply(lambda x: 'Yes' if x>35 else 'No')

df['HighSalary']=df['Salary'].apply(lambda x: 'Yes' if x>60000 else 'No')
print(df)


# Aggregation & Analysis
# Average salary by Department
avg_salary=df.groupby('DeptName')['Salary'].mean()
print(avg_salary)

# Count of senior employees per department
senior_count=df.groupby('DeptName')['Senior'].value_counts().unstack(fill_value=0)
print(senior_count)

# Gender distribution per department
gender_dist=df.groupby('DeptName')['Gender'].value_counts().unstack(fill_value=0)
print(gender_dist)


# multi-level aggregation
# Average salary by Department and Gender
avg_salary_gender=df.groupby(['DeptName','Gender'])['Salary'].mean().unstack(fill_value=0)
print(avg_salary_gender)

# Senior employee count by Manager & Department
senior_by_manager=df.groupby(['Manager','DeptName'])['Senior'].value_counts().unstack(fill_value=0)
print(senior_by_manager)


# conditional aggregation

# Count employees with HighSalary by Gender and Dept
high_sal_emp=df[df['HighSalary']=='Yes'].groupby(['Gender','DeptName'])['EmpID'].count().unstack(fill_value=0)
print(high_sal_emp)

# % of seniors in each dept
perc_senior=df.groupby('DeptName')['Senior'].apply(lambda x: (x=="Yes").mean()*100)
print(perc_senior)


# Ranking and Top N analysis

# Top 3 highest-paid employees per department
# Rank employees within department by salary

df['SalaryRankDept']=df.groupby('DeptName')['Salary'].rank(method='dense',ascending=False)
top_3_dept=df[df['SalaryRankDept']<=3].sort_values(['DeptName','SalaryRankDept'])
print(top_3_dept[['DeptName','EmpID','Salary','SalaryRankDept']])


pivot = df.pivot_table(index='DeptName', columns='Gender', values='Salary', aggfunc=['mean','max']) # type: ignore
print(pivot)



# ---------------------------------------------Problem Statements-------------------------------------------------------------------------------

# Find gender pay gap per department.
# Identify managers with highest average salary among their team.
# Determine department contribution to total salary expense.
# Flag employees who are senior, high-salary, and in top 10% salary bracket.
# Generate a pivot table showing # of employees by AgeGroup and SalaryBucket per department.
# Create a rolling or cumulative salary trend if you add a joining date column.

gender_pay_gap=df.pivot_table(index='DeptName',columns='Gender',values='Salary',aggfunc='mean')
gender_pay_gap['Paygap']=gender_pay_gap['M']-gender_pay_gap['F']
print(gender_pay_gap[['M','F','Paygap']])

managers_has=df.groupby('Manager')['Salary'].mean().sort_values(ascending=False)
print(managers_has)

dept_expense=df.groupby('DeptName')['Salary'].sum().sort_values(ascending=False)
print(dept_expense)

salary_threshold=df['Salary'].quantile(0.90)
df['Top10Percent']=df['Salary'].apply(lambda x: 'Yes' if x>=salary_threshold else 'No')
df['EliteEmp']=df.apply(lambda x: 'Yes' if x['Senior']=='Yes' and x['HighSalary']=='Yes' and x['Top10Percent']=='Yes' else 'No',axis=1)
print(df[['EmpID','DeptName','Age','Salary','Senior','HighSalary','Top10Percent','EliteEmp']])

