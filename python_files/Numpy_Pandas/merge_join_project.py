import pandas as pd

employees=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/employees_031025.csv')
department=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/departments_031025.csv')
salaries=pd.read_csv('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/salaries_031025.csv')

# merge employee with department

emp_dept=pd.merge(employees,department,on='DeptID',how='left')
print(emp_dept)

# merge with salaries

full_data=pd.merge(emp_dept,salaries,on='EmpID',how='outer')


full_data[['BaseSalary','Bonus']]=full_data[['BaseSalary','Bonus']].fillna(0)
print(full_data)


# avg salary per dept
avg_salary=full_data.groupby('DeptName')['BaseSalary'].mean()
print(avg_salary)

# emp without salary
missing_salaries=full_data[full_data['BaseSalary']==0]
print(missing_salaries)

