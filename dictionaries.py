# students = {"Alice": 85, "Bob": 90, "Charlie": 78}

# for student in students:
#     print(student)

# for score in students.values():
#     print(score)

# students['Charlie']=82

# students['David']=93

# for student,score in students.items():
#     print(f"Student {student} has scored {score}")


students = [
    {"name": "Alice", "age": 20, "score": 85},
    {"name": "Bob", "age": 21, "score": 97},
    {"name": "Charlie", "age": 19, "score": 78}
]

for student in students:
    print(f" Name - {student['name']}, Age - {student['age']}, Score - {student['score']}")

max_student=max(students,key=lambda s:s['score'])

print(max_student)

for student in students:
    if student['score']+5<=100:
        student['score']+=5
    else:
        student['score']=100

for student in students:
    print(f" Name - {student['name']}, Age - {student['age']}, Score - {student['score']}")