# Day 2: Data Types & Type Casting - Solutions

# 1
x = 10
y = 3.14
z = "Python"
b = True
print(type(x), type(y), type(z), type(b))

# 2
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {"a": 1, "b": 2, "c": 3}
my_set = {1, 2, 3}
print(my_list, my_tuple, my_dict, my_set)

# 3
num = 100
converted = str(num) + " is a number"
print(converted)

# 4
pi_str = "3.14"
pi_float = float(pi_str)
print(pi_float * 2)

# 5
bool_val = True
print(int(bool_val))  # Outputs 1

# 6
# A tuple is immutable (cannot change), a list is mutable (can change).

# 7
original_list = [1, 2, 2, 3]
unique_set = set(original_list)
print("List:", original_list)
print("Set:", unique_set)

# 8
person = {"name": "Srinivas", "age": 25, "country": "USA"}
print(person["name"])
print(person["age"])
print(person["country"])
