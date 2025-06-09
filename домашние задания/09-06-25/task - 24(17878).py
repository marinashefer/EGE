from re import *

with open ('24_17878.txt') as file:
    data = file.readline()

num = r'([6789][06789]*|0)'
pattern = fr'({num}[-*])+{num}'

matches = finditer(pattern, data)
match = [match.group() for match in matches]

print(len(max(match, key=len)))