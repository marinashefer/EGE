with open ('24_4643.txt') as file:
    data = file.readline()

data = data.replace('1', '2').replace('A', 'B')
data = data.replace('22B', '*')

for i in '2B':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))