class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def introduce(self):
        print(f'Hi! My name is {self.name} and i am {self.age}yrs old.')

class student(person):

    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks

    def average(self):
        return sum(self.marks)/len(self.marks)
    
    def introduce(self):
        super().introduce()
        # print(f'My average score is {self.average()}')


class teacher(person):
    
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    
    def introduce(self):
        super().introduce()
        print(f'I will be teaching you {self.subject} subject')


s1=student('Ishan',29,[98,94,96])
s1.introduce()
print(f'Average marks - {round(s1.average(),2)}')

t1=teacher('Aarav',54,'Math')
t1.introduce()    