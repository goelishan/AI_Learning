class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def info(self):
        return f'Name: {self.name}, Age: {self.age}'
    
class student(person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id

    def info(self):
        base=super().info()
        return f'{base}, Student ID: {self.student_id}'

class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    
    def info(self):
        base=super().info()
        return f'{base}, Subject: {self.subject}'

class sports:
    def __init__(self,sport):
        self.sport=sport
    
    def show_sports(self):
        return f'Plays: {self.sport}'

class sporty_student(student,sports):
    def __init__(self, name, age, student_id,sport):
        student.__init__(self,name,age,student_id)
        sports.__init__(self,sport)

    def info(self):
        base=super().info()
        return f'{base}, {self.show_sports()}'
    
s1=student('ishan',30,'S101')
t1=teacher('Aarav',45,'English')
s2=sporty_student('Riya',28,'S102','Badminton')

print(s1.info())
print(s2.info()) 
print(t1.info())       