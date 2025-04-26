from re import *

with open ('24-8100.txt') as file:
    data = file.readline()

a = r'([1-9][0-9]*[^05+()-])'
b = r'([1-9][0-9]*[05])'

pattern = fr'(\({a}[+-]{b}\))+'
matches = finditer(pattern, data)

print(len(max([i.group() for i in matches], key=len)))