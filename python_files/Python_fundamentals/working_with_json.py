# # JSON - JavaScript Object Notation

# import json

# data = {
#     "students": [
#         {"name": "Ishan", "age": 27, "grade": "A"},
#         {"name": "Aarav", "age": 25, "grade": "B"}
#     ]
# }

# # Write to a JSON file
# with open("output.json", "w") as f:
#     json.dump(data, f, indent=4)  # indent=4 makes it readable


# # reads from JSON file
# with open('data.json','r') as f:
#     data=json.load(f)

# # print(data)
# # print(data['students'][0]['name'])


# json_str='{"name": "Ishan", "age": 27, "grade": "A"}'

# py_obj=json.loads(json_str)
# print(py_obj['name'])

# json_out=json.dumps(py_obj,indent=2)
# print(json_out)
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# Exercise

# Load a JSON file of students.
# Add a new student.
# Calculate the average age.
# Save the updated JSON back to file.

import json

with open('students.json','r') as f:
    data=json.load(f)

print('Students list -')
for row in data['students']:
    print(row)

new_student={'name':'Meera','age':26,'grade':'C'}

data['students'].append(new_student)

total_age=sum(stu['age'] for stu in data['students'])

avg_age=total_age/len(data['students'])

print(f'Average age in data set - {avg_age}')

with open('students.json','w',newline='') as f:
    json.dump(data,f,indent=4)

print('Json write completed.')