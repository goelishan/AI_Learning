# numbers=[2,66,45,78,34,65,89,96]
# names=['ishan','vinay','nirnay','vishal']
# mixed=[1,'hello',3.5,True]

# for name in names:
#     print(f'hello {name}')

# # square of number 1-5

# squares=[x**2 for x in range(1,6)]
# print(squares)

# cubes=[x**3 for x in range(1,5)]
# print(cubes)


# Exercise with list

# numbers=list(range(1,11))
# new_list=[]
# for x in numbers:
#     if x%2==0:
#         new_list.append(x)
# print(new_list)

# numbers.append(11)
# print(numbers)

# numbers.remove(5)
# print(numbers)

# sq_numbers=[]
# for x in numbers:
#     sq_numbers.append(x**2)

# print(sq_numbers)


numbers=list(range(1,11))

even_numbers=[x for x in numbers if x%2==0]

sq_numbers=[x**2 for x in numbers]

print(even_numbers)
print(sq_numbers)