# Day 6: Python Collections — Solutions

# 1
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
print(fruits[2])

# 2
fruits.append('grape')
fruits.remove('banana')
print(fruits)

# 3
colors = ('red', 'green', 'blue')
print(colors[1])

# 4
nums = {1, 2, 3}
nums.add(3)  # no effect
print(nums)

# 5
nums.discard(2)
print(nums)

# 6
person = {'name': 'Srinivas', 'age': 25, 'city': 'New York'}
print(person['name'], person['age'], person['city'])

# 7
person['age'] = 26
print(person)

# 8
for k, v in person.items():
    print(k, ":", v)

# 9
num_list = [1, 2, 2, 3]
num_set = set(num_list)
new_list = list(num_set)
print(new_list)

# 10
student = {
    "id": 1,
    "name": "Srinivas",
    "grades": {"math": 90, "science": 85}
}
print(student)
