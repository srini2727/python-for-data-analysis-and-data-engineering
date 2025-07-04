# Day 3: Control Flow - Solutions

# 1
num = -5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# 3
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4
age = 16
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")

# 5
n = 15
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by 3 and 5")

# 6
username = input("Enter username: ")
if username == "admin":
    print("Welcome Admin")

# 7
a = 10
b = 20
if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("Both are equal")

# 8
n = 4
if n > 0:
    if n % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")

# 9
grade = "B"
if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Good")
elif grade == "C":
    print("Average")
else:
    print("Needs Improvement")

# 10
score = int(input("Enter your score (0–100): "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")
