# Create a list of 5 numbers.

# Replace the 3rd element with a new number.

# Remove the last element.

# Print the final list.

# numbers=[10,20,30,40,50]

# numbers[2]=35

# numbers.pop()

# print(numbers)

# tuple_numbers=tuple(numbers)

# print(tuple_numbers)

# tuple_numbers[0]=15


# Create a list: [5, 2, 9, 1, 5, 6]

# Append 7 to the list.

# Remove the first 5.

# Sort the list in descending order.

# Count how many times 5 appears.

# Find the index of 9.

# Reverse the list and print it.

numbers=[5, 2, 9, 1, 5, 6]
numbers.append(7)
numbers.remove(5)
numbers.sort(reverse=True)
print(numbers)
print(numbers.count(5))
print(numbers.index(9))

numbers.reverse()
print(numbers)
