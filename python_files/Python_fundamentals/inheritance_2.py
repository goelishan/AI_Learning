class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def info(self):
        return f'Name: {self.name}, Age: {self.age}'

class teacher(person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.courses=[]

    def assign_course(self,course):
        self.courses.append(course)
    
    def info(self):
        base=super().info()
        course_name=[c.name for c in self.courses]
        return f'{base}, Teaches:{','.join(course_name) if course_name else 'No courses'}'
    

class student(person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
        self.courses=[]
    
    def enroll(self,course):
        self.courses.append(course)
        course.add_student(self)
    
    def info(self):
        base=super().info()
        course_name=[c.name for c in self.courses]
        return f'{base},student_id: {self.student_id},enrolled in :{','.join(course_name) if course_name else 'No courses'}'

class sports:
    def __init__(self,sportName):
        self.sportName=sportName

    def sport_info(self):
        return f'Plays: {self.sportName}'
    
class sporty_student(student,sports):
    def __init__(self,name,age,student_id,sportName):
        student.__init__(self,name,age,student_id)
        sports.__init__(self,sportName)
    
    def info(self):
        base=super().info()
        return f'{base}, {self.sport_info()}'

class courses:
    def __init__(self,name):
        self.name=name
        self.teacher=None
        self.students=[]

    def assign_teacher(self,teacher):
        self.teacher=teacher
        teacher.assign_course(self)
    
    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
    
    def course_info(self):
        teacher_name=self.teacher.name if self.teacher else 'No teacher assigned.'
        student_names=[s.name for s in self.students]
        return f'Course :{self.name}, teacher: {teacher_name}, Students: {','.join(student_names) if student_names else 'No student.'}'



# Create teacher, students, and sporty student
t1 = teacher("Mr. Sharma", 40)
s1 = student("Ishan", 20, "S101")
ss1 = sporty_student("Aarav", 21, "S202", "Football")

# Create courses
math = courses("Mathematics")
science = courses("Science")

# Assign teacher to courses
math.assign_teacher(t1)

# Enroll students
s1.enroll(math)
ss1.enroll(math)
ss1.enroll(science)

# Print info
print(t1.info())
print(s1.info())
print(ss1.info())
print(math.course_info())
print(science.course_info())
