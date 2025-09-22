# def square(x):
#     return x*x

# # lambda

# sq_lambda=lambda x: x*x

# add = lambda a,b:a+b

# print(add(10,5))

# students = [("Ishan", 35), ("Aarav", 65), ("Riya", 95)]

# sorted_stu=sorted(students,key=lambda x:x[1])
# print(sorted_stu)

# --------------------------------------------------------------------------

# numbers = [1, 2, 3, 4, 5]

# sq_num=list(map(lambda x:x**2, numbers ))

# print(sq_num)

# numbers = [10, 25, 30, 45, 50, 65]

# even=list(filter(lambda x: x%2==0,numbers))

# print(even)

# ----------------------------------------------------------------------------

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# product=reduce(lambda x,y: x*y*2,numbers)

# print(product)

# --------------------------------------------------------------------------------

# Use filter to keep only even numbers.
# Use map to square those even numbers.
# Use reduce to find the sum of these squares.

# from functools import reduce

# numbers = [3, 7, 12, 18, 21, 25, 30]

# even=list(filter(lambda x:x%2==0, numbers))
# print(even)

# square=list(map(lambda x:x*x,even))
# print(square)

# sq_sum=reduce(lambda x,y:x+y,square)
# print(sq_sum)
# ------------------------------------------------------------------------------------------

# Use map to calculate the average score of each student.
# Use filter to keep only students who passed (average ≥ 50).
# Use reduce to calculate the total of all passing averages.

# students = {
#     "Ishan": [45, 60, 72],
#     "Aarav": [30, 40, 42],
#     "Riya": [85, 90, 92],
#     "Maya": [50, 55, 58]
# }

# from functools import reduce

# # average
# averages=list(map(lambda item: (item[0], sum(item[1])/len(item[1])), students.items()))
# print('averages -> ',averages)

# passed=list(filter(lambda item: item[1]>=50,averages))
# print('Passes ->',passed)

# total=reduce(lambda x,y: x+y[1],averages,0)
# print(total)
# ----------------------------------------------------------------------------------------------------------------

# Filter out students who passed (marks >= 50).
# Map the passed students to a new structure where their marks are squared (just for fun 😃).
# Example: ("Aarav", 72) → ("Aarav", 5184)
# Reduce to calculate the total of squared marks of all passed students.
# Finally, print:
# List of passed students
# List of squared marks
# The sum of squared marks

# from functools import reduce

# students = [
#     ("Ishan", 45),
#     ("Aarav", 72),
#     ("Meera", 90),
#     ("Kabir", 33),
#     ("Anaya", 67),
#     ("Rohan", 88),
#     ("Diya", 54)
# ]

# passed=list(filter(lambda item: item[1]>=50,students))
# print(passed)

# sq_marks=list(map(lambda item:(item[0], item[1]*item[1]),passed))
# print(sq_marks)

# total=reduce(lambda x,y:x+y[1],sq_marks,0)
# print(total)

# ---------------------------------------------------------------------------------------------------------------------------------

# Filter only passed students (marks ≥ 50).
# Map them into squared marks.
# Reduce to calculate both total and average of squared marks.
# Find the topper (highest squared marks).

students = [
    ("Aarav", 72),
    ("Meera", 90),
    ("Kabir", 45),
    ("Anaya", 67),
    ("Rohan", 88),
    ("Diya", 54),
    ("Vivaan", 32)
]

from functools import reduce

passed=list(filter(lambda item: item[1]>=50,students))
print(passed)

sq_marks=list(map(lambda item: (item[0],item[1]*item[1]),passed))
print(sq_marks)

total_sq=reduce(lambda x,y:x+y[1],sq_marks,0)
print(total_sq)

avg_sq=total_sq/len(sq_marks)
print(avg_sq)

topper=reduce(lambda x,y: x if x[1]>y[1] else y,sq_marks)

print(topper)

# better method combina map and filter
sq_marks_1=list(map(lambda item: (item[0],item[1]**2), filter(lambda item: item[1]>=50,students)))
print(sq_marks_1)

