# students = {
#     "Ishan": [85, 92, 78],
#     "Aarav": [65, 70, 72],
#     "Riya": [95, 90, 93],
#     "Maya": [40, 50, 45]
# }


# # Takes a dictionary of students with marks.
# # Calculates their average
# # Assigns a grade:
# # A: 90+
# # B: 75–89
# # C: 50–74
# # F: below 50
# # Returns a new dictionary with student name → grade.


# def grade_students(student_data):
#     grades={}

#     for name,marks in student_data.items():
#         avg=sum(marks)/len(marks)

#         if avg>=90:
#             grade='A'
#         elif avg>=75:
#             grade='B'
#         elif avg>=50:
#             grade='C'
#         else:
#             grade='F'
        
#         grades[name]=grade

#     return grades

# results=grade_students(students)
# print(results)

# -----------------------------------------------------------------------------------------------------------------------
# Write a function that:
# Takes a string (the paragraph).
# Splits it into words.
# Counts how many times each word appears.
# Returns a dictionary where:
# key = word
# value = count

# def count_words(text):

#     checker=text.lower()

#     word_collection={}
#     word_collection=checker.split()

#     counter={}

#     for word in word_collection:
#         if word in counter:
#             counter[word]+=1
#         else:
#             counter[word]=1
    
#     return counter

# result = count_words("Python is fun and Python is powerful")

# print(result)

# ----------------------------------------------------------------------------------------------------------------------------------

# def introduce(name, age=25, *hobbies):
#     print(f'{name} has age - {age}')

#     for hobbies in hobbies:
#         print(hobbies)

# introduce('ishan',30,'Cricket','F1','sleeping')


# -----------------------------------------------------------------------------------------------------------------------------------
def introduce(name, age=25, *hobbies, **extra_info):

    print(f'{name} has age - {age}')

    for hobbie in hobbies:
        print(hobbie)

    for key,value in extra_info.items():
        print(f'{key} -> {value}')

introduce(
    "Ishan",
    30,
    "Cricket",
    "F1",
    city="Delhi",
    profession="Engineer"
)
