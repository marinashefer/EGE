from re import finditer

with open ('24_4627.txt') as file:
    data = file.readline()

pattern = r'(NPO|PNO)+'
matches = finditer(pattern, data)

matches = [i.group() for i in matches]
print(len(max(matches, key=len))//3) #делим на 3, так как ищем последовательности