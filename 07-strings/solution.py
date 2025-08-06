# Python String Solutions (Day 7)
name = "Srinivas"
print(name)
print(name.upper(), name.lower())

msg = "  Hello  "
print(msg.strip())

text = "I love Python"
print(text.replace("Python", "SQL"))

fruits = "apple,banana,cherry"
print(fruits.split(","))

sample = "DataEngineering"
print(sample[:5])

sentence = "Data is powerful"
print("data" in sentence.lower())

word = "banana"
print(word.count("a"))

first, last = "Srinivas", "Reddy"
print(f"My name is {first} {last}")

word = "analytics"
print(word[::-1])
