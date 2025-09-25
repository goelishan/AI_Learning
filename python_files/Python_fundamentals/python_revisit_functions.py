# factorial function

def factorial_interative(num):
    fact=1
    for n in range(1,num+1):
        fact=fact*n
    return fact

def factorial_recursive(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial_recursive(num-1)

print(factorial_interative(10))
print(factorial_recursive(10))


# Average of set of numbers

def calc_avg(num):
    if len(num) == 0:
        return 0
    else:
        return sum(num)/len(num)
    
print(calc_avg([1,2,3,4,5,6]))


# Write a function that prints profile details
def profile(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

profile(name="Ishan", age=29, city="Delhi")

# sorting with lambda

def sorted_students(students):

   return sorted(students, key=lambda x:x[1],reverse=True)
   

students = [("Aman", 85), ("Neha", 92), ("Raj", 78)]
print(sorted_students(students))
    