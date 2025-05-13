with open ('24_6054.txt') as file:
    data = file.readline()

data = data.replace('B', 'C')
data = data.replace('CCA', '***')

for i in 'ABC':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))