with open ('24_4627.txt') as file:
    data = file.readline()

while 'NPO' in data or 'PNO' in data:
    data = data.replace('NPO', '*')
    data = data.replace('PNO', '*')

for i in 'NPO':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))