# Sets are collection of unique and unordered items

# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A | B)   # Union → {1, 2, 3, 4, 5}
# print(A & B)   # Intersection → {3}
# print(A - B)   # Difference → {1, 2}
# print(A ^ B)   # Symmetric Difference → {1, 2, 4, 5}


# data = ["Python", "SQL", "Python", "AI", "SQL", "ML"]

# unique_skills = set(data)
# print(unique_skills)  # {'Python', 'SQL', 'AI', 'ML'}


# ------------------------------------------------------------------------------------------------------------

ishan_skills = {"Python", "SQL", "AWS"}
aarav_skills = {"Java", "Python", "SQL"}
riya_skills  = {"AWS", "GCP", "Python"}

# Find all unique skills in the company.
# Find common skills between all employees.
# Find skills that Ishan knows but Aarav doesn’t.
# Check if Riya’s skills are a subset of all company skills.

print(ishan_skills|aarav_skills|riya_skills)
print(ishan_skills & aarav_skills & riya_skills)
print(ishan_skills - aarav_skills)
print(riya_skills.issubset(ishan_skills|aarav_skills|riya_skills))