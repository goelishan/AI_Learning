# # Normal way

# num=[]
# for i in range(1,6):
#     num.append(i*i)
# print(num)

# # comprehension

# num1=[i*i for i in range(1,6)]
# print(num1)

# # dictionary comprehension

# squares={i: i*i for i in range(1,6)}

# print(squares)

# # set comprehension

# set={i*i for i in [1,2,2,3,4,5]}

# print(set)

# --------------------------------------------------------------------------------------------------------------------------

# numbers = [12, 7, 5, 64, 14, 9, 33]

# even=[n for n in numbers if n%2==0]
# print(even)

# sq_odd=[n*n for n in numbers if n%2!=0]
# print(sq_odd)

# double=[n*2 for n in numbers if n>10]
# print(double)

# -----------------------------------------------------------------------------------------------------------------------------

# numbers = [10, 15, 22, 33, 40, 55]

# result=['even -'+str(n) if n%2==0 else 'odd - '+str(n) for n in numbers]

# print(result)

# -------------------------------------------------------------------------------------------------------------------------------
students = {
    "Ishan": 85,
    "Aarav": 45,
    "Riya": 92,
    "Maya": 50
}


result={key:('Pass' if value>=50 else 'Fail') for key,value in students.items()}

result1={key:{'score': value, 'status':'Pass' if value>=50 else 'Fail'} for key,value in students.items()}

# print(result)

# print(result1)

passed={key: value for key,value in students.items() if value>=50}

failed={key: value for key,value in students.items() if value<50}

# print(passed)
# print(failed)

passed_detail={key:{'score':value, 'status':'Pass'} for key,value in students.items() if value>=50}

failed_detail={key:{'score':value, 'status':'fail'} for key,value in students.items() if value<50}

print(passed_detail)
print(failed_detail)