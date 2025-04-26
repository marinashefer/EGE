from re import *

with open ('24-8060.txt') as file:
    data = file.readline()

a = r'@yandex[.]ru'
b = r'@gmail[.]com'

pattern = fr'(\w+[.])*\w+({a}|{b})'
matches = finditer(pattern, data)

print(len(max([i.group() for i in matches], key= len)))