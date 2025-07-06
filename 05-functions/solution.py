# Day 5: Python Functions — Solutions

# 1
def add(a, b):
    return a + b

# 2
def square(n):
    return n * n

# 3
def greet(name):
    print(f"Hello, {name}!")

# 4
def is_even(n):
    return n % 2 == 0

# 5
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 6
def sum_list(numbers):
    return sum(numbers)

# 7
def describe_country(name="USA"):
    return f"Country is {name}"

# 8
def find_max(*args):
    return max(args)

# 9
def is_palindrome(s):
    return s == s[::-1]

# 10
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator"
