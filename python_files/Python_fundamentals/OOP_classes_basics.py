class Student:

    def __init__(self, name, math, science, english) -> None:
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def total_marks(self):
        return int(self.math) + int(self.science) + int(self.english)

    def display(self):
        print(f'{self.name} -> Total Marks - {self.total_marks()}')


# working with csv file in class
import csv

students = []

with open('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/marks.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            math = int(row['Math'])
            science = int(row['Science'])
            english = int(row['English'])   

            stud = Student(row['Name'], math, science, english)
            students.append(stud)

        except ValueError:
            bad_field = []
            for subject in ['Math', 'Science', 'English']:
                try:
                    int(row[subject])
                except ValueError:
                    bad_field.append(f"{subject} = {row[subject]}")  

            print(f"Skipping {row['Name']} due to bad field in {', '.join(bad_field)}")  


# Display only valid students
for s in students:
    s.display()
