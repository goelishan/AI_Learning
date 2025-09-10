# students = {
#     "101": {"name": "Ishan", "age": 27},
#     "102": {"name": "Aarav", "age": 25}
# }

# print(students["101"]["name"])   # Ishan


# for roll in students.keys():
#     print('Roll no. ',roll)


# for roll,info in students.items():
#     print('Roll No. ',roll, 'Name - ',info['name'], 'Age - ',info['age'])

# ---------------------------------------------------------------------------------------------------

# employees = {
#     "E101": {"name": "Ravi", "dept": "IT", "salary": 60000},
#     "E102": {"name": "Neha", "dept": "HR", "salary": 55000},
#     "E103": {"name": "Amit", "dept": "Finance", "salary": 65000}
# }

# # Print only the employee IDs (E101, E102, …).

# # Print only the salaries.

# for ids in employees.keys():
#     print('Emp Ids -',ids)

# for ids,sal in employees.items():
#     print('Salary - ',sal['salary'])

# for ids,info in employees.items():
#     print(f'{info['name']} works in {info['dept']} and earns {info['salary']}')

# --------------------------------------------------------------------------------------------------------------

# employees = {
#     "E101": {"name": "Ravi", "dept": "IT", "salary": 60000},
#     "E102": {"name": "Neha", "dept": "HR", "salary": 55000},
#     "E103": {"name": "Amit", "dept": "Finance", "salary": 65000},
#     "E104": {"name": "Sonia", "dept": "IT", "salary": 72000}
# }

# # Print only the names of employees who earn more than 58000.

# # Print names of employees who are in the IT department.

# for ids,info in employees.items():
#     if info['salary']>58000:
#         print(info['name'])

# for ids,info in employees.items():
#     if info['dept']=='IT':
#         print(info['name'])


# dept_emp={}

# for ids,info in employees.items():
#     dept=info['dept']
#     name=info['name']

#     if dept not in dept_emp:
#         dept_emp[dept]=[]
    
#     dept_emp[dept].append(name)


# for dept,name in dept_emp.items():
#     print(f'{dept} -> {name}')

# ---------------------------------------------------------------------------------------------------------------------------

employees = {
    "E101": {"name": "Ravi", "dept": "IT", "salary": 60000},
    "E102": {"name": "Neha", "dept": "HR", "salary": 55000},
    "E103": {"name": "Amit", "dept": "Finance", "salary": 65000},
    "E104": {"name": "Sonia", "dept": "IT", "salary": 72000}
}

# Find the department with the highest total salary.
# (Add salaries of employees department-wise, then figure out which dept has the largest total.)

# Print department-wise salary totals like this:

sal_dist={}

for ids,info in employees.items():
    dept=info['dept']
    sal=info['salary']

    if dept not in sal_dist:
        sal_dist[dept]=0
    
   
    sal_dist[dept]+=sal
    
for dept,total in sal_dist.items():
    print(f'{dept} -> {total}')
    

highest_sal = max(sal_dist, key=lambda d: sal_dist[d])

print(f'Department with highest salaries - {highest_sal} ({sal_dist[highest_sal]})')

