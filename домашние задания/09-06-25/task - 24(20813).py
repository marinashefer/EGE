from re import *

with open ('24_20813.txt') as file:
    data = file.readline()

num = r'([789][0789]*|0)'
pattern = fr'({num}[-*])+{num}'

matches = finditer(pattern, data)
match = [match.group() for match in matches]

print(len(max(match, key=len)))

