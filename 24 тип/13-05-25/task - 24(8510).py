with open ('24_8510.txt') as file:
    data = file.readline()

data = data.replace('N', 'P').replace('O', 'P')

while 'PP' in data:
    data = data.replace('PP', 'P P')

data = data.split()
print(len(max(data, key=len)))