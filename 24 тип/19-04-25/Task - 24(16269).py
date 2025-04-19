with open('24_16269.txt') as file:
    data = file.readline()

for i in 'TUVW':
    data = data.replace(i, ' ')

while 'XXX' in data or 'YYY' in data or 'ZZZ' in data:
    data = data.replace('XXX', 'XX XX')
    data = data.replace('YYY', 'YY YY')
    data = data.replace('ZZZ', 'ZZ ZZ')

data = data.split()
print(len(max(data, key=len)))