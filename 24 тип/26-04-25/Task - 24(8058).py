from re import *

with open('24-8058.txt') as file:
    data = file.readline()

pattern = r'[ABC][abc]* ([ABC]?[abc]+ )*[ABC]?[abc]*[.]'
matches = finditer(pattern, data)

print(len(max([i.group() for i in matches], key=len)))