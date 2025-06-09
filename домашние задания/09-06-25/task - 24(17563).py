from re import *

with open ('24_17563.txt') as file:
    data = file.readline()

num = r'([789][0789]*)'
pattern = fr'({num}[-*])+{num}'

matches = finditer(pattern, data)
match = [match.group() for match in matches]

print(len(max(match, key=len)))