with open ('24_4710.txt') as file:
    data = file.readline()

for i in 'CD':
    data = data.replace('C', 'F').replace('D', 'F')

data = data.replace('A', 'O')

data = data.replace('FO', '*')

for i in 'ACDFO':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))