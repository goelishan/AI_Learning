import csv

with open('marks.csv','w',newline='') as f:
    writer=csv.writer(f)

    writer.writerow(['Name','Math','Science','English'])
    writer.writerow(['Ishan',85,90,88])
    writer.writerow(['Aarav',78,82,89])
    writer.writerow(['Riya',92,95,91])
    writer.writerow(['Meera',88,76,84])

# Print highest scorer
# with open('marks.csv','r') as f:
#     reader=csv.DictReader(f)

#     top_student=None
#     top_marks=0

#     for row in reader:
#         total=int(row['Math'])+int(row['Science'])+int(row['English'])
    
#         if total>top_marks:
#             top_marks=total
#             top_student=row['Name']

#     print(f'{top_student} is the highest scorer with {top_marks} marks')


# -------------------------------------------------------------------------------------------------------------------

students=[]
# Read data from csv file
with open('marks.csv','r') as f:
    reader=csv.DictReader(f)
    for row in reader:
        total=int(row['Math'])+int(row['Science'])+int(row['English'])
        row['Total']=total
        students.append(row)

# Sort by total

sorted_students=sorted(students,key=lambda x: x['Total'],reverse=True)

with open('results.csv','w',newline='') as f:
    fieldnames=['Rank','Name','Math','Science','English','Total']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()

    for i,students in enumerate(sorted_students,start=1):
        writer.writerow({
            'Rank':i,
            'Name':students['Name'],
            'Math':students['Math'],
            'Science':students['Science'],
            'English':students['English'],
            'Total':students['Total']
        })

    

print('Results have been published to results.csv file!')



