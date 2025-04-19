from re import *

with open ('24_18597.txt') as file:
    data = file.readline()

pattern = r'[1-9][0-9]{3}[.][0-9]+[&][1-9][0-9]{3}[.][0-9]+'
pattern2 = r'[1-9]\d{3}\.[0-9]+[&][1-9]\d{3}\.+'

matches = finditer(pattern, data)

print(max(len(i.group()) for i in matches))