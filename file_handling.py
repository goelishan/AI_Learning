# with open("Students.txt",'w') as file:
#     file.write('Ishan,85\n')
#     file.write('Aarav,69\n')
#     file.write('Riya,87\n')
#     file.write('Maya,93\n')


# with open('Students.txt','r') as file:
#     for line in file:
#         name,score = line.strip().split(',')
#         print(f"Name ->{name},\tScore ->{score}")



# with open("students.txt",'r') as file:
#     line1=file.readline()
#     line2=file.readline()

#     print(f'Line 1 -> {line1}')
#     print(f'Line 2 -> {line2}')

# with open("students.txt",'r') as f:
#     lines=f.readlines()
#     print(lines)

# with open('students.txt','r') as f:
#     for line in f:
#         print(line.strip())

# with open('students.txt','r') as f:
#     print(f.tell())
#     f.read(5)
#     print(f.tell())

# with open('students.txt','r') as f:
#     f.seek(5)
#     print(f.read(5))

with open('students.txt','rb') as f:
    f.seek(-5,2)
    print(f.read())