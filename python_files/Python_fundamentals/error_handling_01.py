def divide(a,b):

    try:
        result=a/b
    except ZeroDivisionError:
        print('cannot divide by 0!')
       
    except TypeError:
        print('inputs must be number!')
        
    else:
        print('Division successful.')
        return result
    finally:
        print('Divide module reached finally block')


print(divide(10,2))
print(divide(10,0))
print(divide(10,'a'))