# Task: Write a function analyze_scores that:
# Takes a dictionary of students as a required argument.
# Takes an optional parameter passing_mark (default = 50).
# Accepts any number of extra keyword arguments like bonus=5 or round_avg=True.
# Returns a dictionary where for each student:
# "average" → their average (apply bonus if passed)
# "passed" → True if average ≥ passing_mark, else False

# def analyze_scores(students,passing_mark=50,**options):

#     grade_student={}

#     bonus=options.get("bonus",0)

#     for name,marks in students.items():
#         avg=sum(marks)/len(marks)
    
#         avg+=bonus

        
#         passed=avg>=passing_mark

#         grade_student[name]={
#             "average":avg,
#             'passed':passed
#         }
#     return grade_student


# students = {
#     "Ishan": [85, 92, 78],
#     "Aarav": [65, 70, 72],
#     "Riya": [95, 90, 93],
#     "Maya": [40, 50, 45]
# }

# print(analyze_scores(students))
# print(analyze_scores(students, passing_mark=60))
# print(analyze_scores(students, bonus=5))

# ------------------------------------------------------------------------------------------------------------------------------

# Write a function merge_dicts that:
# Takes any number of dictionaries as *args.
# If the same key appears in multiple dictionaries:
# If values are numbers, add them together.
# If values are lists, merge them into one list.
# Otherwise, keep the last value.
# Returns a single merged dictionary.

def merge_dicts(*dicts):
    merged={}

    for d in dicts:

        for key,value in d.items():
            if key in merged:
                if isinstance(value, (int,float)) and isinstance(merged[key],(int,float)):
                    merged[key]+=value
                
                elif isinstance(value,list) and isinstance(merged[key],list):
                    merged[key].extend(value)

                else:
                    merged[key]=value
            else:
                merged[key]=value
    return merged






dict1 = {"a": 10, "b": [1, 2], "c": "hello"}
dict2 = {"a": 5, "b": [3], "c": "world", "d": 50}
dict3 = {"a": 7, "b": [4, 5], "e": "new"}

print(merge_dicts(dict1, dict2, dict3))