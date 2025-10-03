# Create a toolkit that can evaluate nested math operations dynamically, 
# including addition, multiplication, subtraction, division, and exponentiation.

# Functions calling themselves recursively
# Handling *args dynamically
# Handling nested dictionaries
# Returning computed results
# Optional: Use **kwargs for default behaviors

def evaluate_expression(expr):

    def apply_op(op,*values):

        if op=='add':
            return sum(values)
        elif op=='multiply':
            result=1
            for v in values:
                result*=v
            return result
        elif op=='subtract':
            res=values[0]
            for v in values[1:]:
                res-=v
            return res
        elif op=='divide':
            res=values[0]
            for v in values[1:]:
                res/=v
            return res
        elif op=='power':
            base,exponent=values
            return base**exponent
        else:
            raise ValueError(f'Invalid operation: {op}')
    
    computed_values=[]

    for val in expr['values']:

        if isinstance(val,dict):
            computed_values.append(evaluate_expression(val))
        else:
            computed_values.append(val)
    
    return apply_op(expr['operation'],*computed_values)


expression = {
    "operation": "add",
    "values": [
        2,
        3,
        {
            "operation": "multiply",
            "values": [2, 5]
        },
        {
            "operation": "power",
            "values": [3, 2]
        },
        {
            "operation": "subtract",
            "values": [20, 5]
        }
    ]
}

# 2+3+(2*5)+(3^2)+(20-5)

result = evaluate_expression(expression)
print("Result:", result)