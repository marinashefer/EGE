from re import *

with open ('24_15339.txt') as file:
    data = file.readline()

pattern = r'([ABC][6-9])+[ABC]?|([6-9][ABC])+[6-9]?'
matches = finditer(pattern, data)

print(max(len(i.group()) for i in matches))