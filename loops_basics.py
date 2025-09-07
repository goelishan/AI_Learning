# Even / Odd numbers
for i in range(1, 11):
    print(f"{i} is {'even' if i % 2 == 0 else 'odd'}")

# Countdown using while
count = 8
while count:
    print(f"Countdown - {count}")
    count -= 1

# Odd numbers (1 to 30)
for i in range(1, 31, 2):
    print(f"{i} is odd")

# Sum of Numbers
total = sum(range(1, 101))
print(f"Sum of 1 to 100 = {total}")

# Multiplication table of 7
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")

# Numbers divisible by 3
for i in range(3, 51, 3):
    print(i)
