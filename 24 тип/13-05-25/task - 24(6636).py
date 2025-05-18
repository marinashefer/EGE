with open ('24_6636.txt') as file:
    data = file.readline()

for i in '13':
    data = data.replace(i, '5')

data = data.replace('4', '2')
data = data.replace('25', '*')

for i in '12345':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))