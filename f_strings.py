# name='Ishan'
# score=93

# print(f'{name} has scored {score} in his last exam.')

# print(f'With practise you can aim for {score+5}')

# format method

# name='Ishan'
# score=90

# print('{0} has scored {1} marks in his exam, {0} can do well next time.'.format(name,score))


# pi = 3.1415926535

# print(f'pi rounded to 2 decimal places : {pi:.2f}')

# print('Pi rounded to 3 decimal places : {:.3f}'.format(pi))


# name = "Alice"
# age = 30
# height = 5.6789

# print(f'{name} is {age} years old and {height:.1f} ft tall')

# print('{0} is {1} years old and {2:.1f} ft tall'.format(name,age,height))


quote = "Artificial Intelligence with Python"

# Slice out "Artificial" and "Python" from the string.

# Count how many times the letter "i" (case-insensitive) appears in the string.

# Replace "Intelligence" with "Learning".

# Print the string in title case (first letter of each word capitalized).

# Using an f-string, print:
# "The phrase 'Artificial Intelligence with Python' has X characters."
# (where X is the length of the string).

# for index,char in enumerate(quote):
#     print(index,char)

# print(quote[0:10])
# print(quote[29:])

# print(quote.replace('Intelligence','Learning'))

# print(quote.lower().count('i'))

# print(quote.title())

# print(f"The phrase '{quote}' has {len(quote)} characters")

full_name = "Sir Alan Mathison Turing"

# Tasks:

# Slice out the first name, middle name, and last name separately.

# Extract the initials → "A.M.T."

# Print a formatted sentence using an f-string:

# The initials of Alan Mathison Turing are A.M.T.


parts=full_name.split()
print(parts)

initials=parts[0][0]+'.'+parts[1][0]+'.'+parts[2][0]+'.'

print(f'The initials of {full_name} are {initials}')


initials_1='.'.join([p[0] for p in parts])+'.'

print(f'The initials of {full_name} are {initials_1}')