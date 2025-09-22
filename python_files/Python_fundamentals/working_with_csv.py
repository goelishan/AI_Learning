# import csv

# with open('csv_basics.csv','w',newline='') as f:
#     writer=csv.writer(f)
#     writer.writerow(['Name','Age','Grade'])
#     writer.writerow(['Ishan',27,'A'])
#     writer.writerow(['Aarav',25,'B'])


# with open('csv_basics.csv','r') as f:
#     reader=csv.reader(f)
#     for row in reader:
#         print(row)


# -----------------------------------------------------------------
# Dictionary-Based CSV Handling


import csv

with open('student_dict.csv','w',newline='') as f:
    fieldnames=['Name','Age','Grade']
    writer=csv.DictWriter(f,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name':'Ishan','Age':27,'Grade':'A'})
    writer.writerow({'Name':'Aarav','Age':25,'Grade':'B'})


with open('student_dict.csv','r') as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row)