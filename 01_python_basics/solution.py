# 1
name = "Srini"
age = 27
country = "India"
print(f"My name is {name}, I'm {age} years old from {country}.")

# 2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum: {num1 + num2}, Difference: {num1 - num2}, Product: {num1 * num2}")

# 3
temperature_celsius = 30.5
fahrenheit = temperature_celsius * 9/5 + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# 4
print(type(25))
print(type("hello"))
print(type(3.14))
print(type(True))

# 5
s = "123"
i = int(s)
print(i * 2, type(i))

# 6
full_name = input("Enter your full name: ")
print(full_name.upper())
print(full_name.lower())
print(full_name.title())

# 7
birth_year = int(input("Enter your birth year: "))
current_year = 2025
print(f"Your approximate age is: {current_year - birth_year}")

# 8
price = 49.99
print(f"Price: ${price:.2f}")

# 9
color = input("Favorite color? ")
food = input("Favorite food? ")
print(f"You love {color} and enjoy eating {food}!")

# 10
radius = 5
pi = 3.14159
area = pi * radius ** 2
print(f"Area of circle: {area}")

# 11
print(bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1, 2]))

# 12
num = float(input("Enter a number: "))
print(f"Is the number greater than 100? {num > 100}")
