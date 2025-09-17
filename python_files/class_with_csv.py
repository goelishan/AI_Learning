import csv

class student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def total_marks(self):
        return sum(self.marks)
    
    def average(self):
        return sum(self.marks)/len(self.marks)
    
    def display(self):
        print(f'Name - {self.name}, total marks - {self.total_marks()}, average - {round(self.average(),2)}')


students=[]
csv_file='C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/marks.csv'

with open(csv_file,'r') as f:
    reader=csv.DictReader(f)

    for row in reader:
        try:
            marks=int(row['Math']),int(row['Science']),int(row['English'])
            stud=student(row['Name'],marks)
            students.append(stud)
        except ValueError:
            print(f'skipping {row['Name']} due to bad values')


print('All students -')
for s in students:
    s.display()
            