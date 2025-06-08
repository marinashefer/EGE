with open ('24_1866.txt') as file:
    data = file.readline()

while 'da' in data or 'ad' in data:
    data = data.replace('ad', 'a d')
    data = data.replace('da', 'd a')

data = data.split()
print(len(max(data, key=len)))