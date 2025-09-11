# dict1 = {"name": "Ravi", "dept": "IT", "salary": 60000}
# dict2 = {"dept": "HR", "location": "Delhi", "salary": 65000}

# # Merge these two dictionaries into a new dictionary.

# # If a key exists in both, the value from dict2 should overwrite dict1.

# # Print the final merged dictionary.

# merged_dict=dict1|dict2

# print(merged_dict)
# ----------------------------------------------------------------------------------------------------------------------


# emp1 = {"name": "Ravi", "dept": "IT", "salary": 60000}
# emp2 = {"name": "Neha", "dept": "HR", "salary": 55000, "location": "Mumbai"}
# emp3 = {"name": "Amit", "dept": "Finance", "salary": 65000}

# # Merge emp1, emp2, and emp3 into a single dictionary of employees, with keys as employee names:

# all_emp=[emp1,emp2,emp3]

# # print(all_emp)

# employee_dict={}

# for emp in all_emp:
#     name=emp['name']

#     if name in employee_dict:
#         employee_dict[name].update(name)
#     else:
#         employee_dict[name]=emp.copy()


# for name,info in employee_dict.items():
#     print(f'{name} -> {info}')

# -----------------------------------------------------------------------------------------------------------------------------

# emp1 = {"name": "Ravi", "info": {"dept": "IT", "salary": 60000}}
# emp2 = {"name": "Neha", "info": {"dept": "HR", "salary": 55000, "location": "Mumbai"}}
# emp3 = {"name": "Ravi", "info": {"location": "Delhi", "salary": 65000}}

# # Merge these dictionaries into a single dictionary keyed by employee name.

# all_emp=[emp1,emp2,emp3]

# merged_emp={}

# for emp in all_emp:
#     name=emp['name']
#     info=emp['info']

#     if name in merged_emp:
#         merged_emp[name]['info'].update(info)
#     else:
#         merged_emp[name]={'info':info.copy()}

# for name,data in merged_emp.items():
#     print(f"{name} -> {data['info']}")

# -------------------------------------------------------------------------------------------------------------------------------------

emp1 = {"name": "Ravi", "info": {"dept": "IT", "salary": 60000, "projects": ["Alpha"], "skills": ["Python"]}}
emp2 = {"name": "Neha", "info": {"dept": "HR", "salary": 55000, "projects": ["Beta"], "skills": ["Communication"]}}
emp3 = {"name": "Ravi", "info": {"salary": 65000, "location": "Delhi", "projects": ["Gamma"], "skills": ["AWS"]}}

# Merge all employees into a single dictionary keyed by employee name.
# Merge nested dictionaries:
# For scalar values like salary or location, the latest value overwrites the old one.
# For lists like projects or skills, concatenate the lists instead of overwriting.
# Print the final merged dictionary like this:

all_emp=[emp1,emp2,emp3]

merged_emp={}

for emp in all_emp:
    name=emp['name']
    info=emp['info']

    if name not in merged_emp:
        merged_emp[name]={'info':{}}

    for key,value in info.items():
        if key in merged_emp[name]['info']:
            if isinstance(value,list):
                merged_emp[name]['info'][key].extend(value)
            else:
                merged_emp[name]['info'][key]=value
        else:
            merged_emp[name]['info'][key]=value if not isinstance(value,list) else value.copy()

for name, data in merged_emp.items():
    print(f"{name} -> {data['info']}")