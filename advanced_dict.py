emp1 = {
    "name": "Ishan",
    "skills": ["Python", "SQL"],
    "projects": {"current": "DB Automation", "previous": ["Inventory App"]}
}

emp2 = {
    "name": "Aarav",
    "skills": ["Java", "Python"],
    "projects": {"current": "Web Portal", "previous": ["HR App", "Inventory App"]}
}

emp3 = {
    "name": "Riya",
    "skills": ["SQL", "AWS"],
    "projects": {"current": "Cloud Migration", "previous": []}
}

# Merge all employees into a single dictionary where the key is the employee name, and all their skills and 
# projects are combined properly (avoid duplicates in lists).

all_emp = [emp1, emp2, emp3]

merged_emp={}

for emp in all_emp:
    name=emp['name']

    if name not in merged_emp:
        merged_emp[name]= {"skills":[],"projects":{"current":None, "previous":[]}}
    
    for skill in emp['skills']:
        if skill not in merged_emp[name]['skills']:
            merged_emp[name]['skills'].append(skill)

    merged_emp[name]['projects']['current']=emp['projects']['current']

    for prev_proj in emp['projects']['previous']:
        if prev_proj not in merged_emp[name]['projects']['previous']:
            merged_emp[name]['projects']['previous'].append(prev_proj)

print(merged_emp)