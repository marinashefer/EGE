from re import *

with open ('24_18284.txt') as file:
    data = file.readline()

pattern = r'L[^L]*?O.*?V.*?E'

matches = finditer(pattern, data)

print(max(len(i.group()) for i in matches))