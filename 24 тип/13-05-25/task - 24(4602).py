with open ('24_4602 (1).txt') as file:
    data = file.readline()

for i in 'AO':
    data = data.replace(i, 'A')

for i in 'BCD':
    data = data.replace(i, 'D')

data = data.replace('DA', '*')
for i in 'ABCDO':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))