# Python File Handling Solutions (Day 8)
# 1
with open('sample.txt','w') as f:
    f.write('Hello, Python')

# 2
with open('sample.txt','r') as f:
    print(f.read())

# 3
with open('sample.txt','r') as f:
    for line in f:
        print(line.strip())

# 4
with open('sample.txt','a') as f:
    f.write('\nNew Line Added')

# 5
with open('sample.txt','r') as f:
    lines = f.readlines()
    print("Line count:", len(lines))

# 6
with open('sample.txt','r') as f:
    words = f.read().split()
    print("Word count:", len(words))

# 7
import csv
with open('sample.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 8
fruits = ['apple','banana','cherry']
with open('fruits.txt','w') as f:
    for fruit in fruits:
        f.write(fruit+'\n')

# 9
with open('sample.txt','r') as src, open('copy.txt','w') as dest:
    dest.write(src.read())

# 10
try:
    with open('nofile.txt','r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
