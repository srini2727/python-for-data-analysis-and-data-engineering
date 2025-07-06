# Day 4: Python Loops — Solutions

# 1
for i in range(1, 11):
    print(i)

# 2
i = 10
while i > 0:
    print(i)
    i -= 1

# 3
for i in range(2, 21, 2):
    print(i)

# 4
for char in "Python":
    print(char)

# 5
nums = [10, 20, 30]
total = sum(nums)
print("Sum:", total)

# 6
person = {"name": "Srinivas", "age": 25}
for key, value in person.items():
    print(key, ":", value)

# 7
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")

# 8
numbers = [1, 3, 7, 9]
for num in numbers:
    if num == 7:
        print("Found 7!")
        break

# 9
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 10
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
