# Using list comprehensions:

# Create a list of squares of numbers from 1 to 10.

# Create a list of even numbers between 1 and 20.

# Convert this list ["deep", "learning", "python"] into uppercase.


# squares=[x**2 for x in range(1,11)]
# print(squares)

# even_no=[x for x in range(1,21) if x%2==0]
# print(even_no)

# check=["deep", "learning", "python"]

# upper=[x.upper() for x in check]
# print(upper)

# ------------------------------------------------------------------------------------------------------------------------------------------
# From numbers 1–20, create a list where even numbers are squared and odd numbers are cubed.
# → Output should look like [1, 4, 27, 16, 125, …]

numbers=[x**2 if x%2==0 else x**3 for x in range(1,21)]
print(numbers)