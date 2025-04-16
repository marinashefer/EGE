from re import finditer

with open ('24_4602.txt') as file:
    data = file.readline()

pattern = r'([BCD][AO])+'

matches = finditer(pattern, data)
matches = [i.group() for i in matches]
print(len(max(matches, key=len))//2) #делим на 2, так как ищем пары, а не символы!