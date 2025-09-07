students = {"Alice": 85, "Bob": 90, "Charlie": 78}

for student in students:
    print(student)

for score in students.values():
    print(score)

students['Charlie']=82

students['David']=93

for student,score in students.items():
    print(f"Student {student} has scored {score}")