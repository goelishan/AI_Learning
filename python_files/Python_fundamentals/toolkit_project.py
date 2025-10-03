# We will implement a toolkit with functions for:
# Sum of numbers (using *args)
# Multiplication of numbers (using *args)
# Average of numbers
# Power function (default exponent)
# A main function that calls all other functions


def sum_of_numbers(*args):
    total=sum(args)
    print(f'Sum of numbers - {total}')
    return total

def multiplication_of_numbers(*args):
    result=1

    for n in args:
        result=result*n
    print(f'Multiplication result - {result}')
    return result

def avg_of_numbers(*args):

    total=sum_of_numbers(*args)
    avg=total/len(args)
    print(f'Avg of numbers - {avg}')
    return avg

def power_func(base,exponent):

    result = base**exponent
    print(f'With {base} to power {exponent} gives {result}')
    return result

def math_toolkit(*args,**kwargs):

    print('Math operation toolkit')

    sum_result=sum_of_numbers(*args)
    multi_result=multiplication_of_numbers(*args)
    avg_result=avg_of_numbers(*args)

    if 'base' in kwargs:
        exp=kwargs.get('exponent',2)
        power_func(kwargs['base'],exp)


math_toolkit(2,3,4,base=5,exponent=3)


