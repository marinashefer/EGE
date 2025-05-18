with open ('24_9845.txt') as file:
    data = file.readline()

data = data.replace('A', 'C').replace('B', 'C')
data = data.replace('9', '8')

while 'CC' in data or '88' in data:
    data= data.replace('CC', 'C C')
    data= data.replace('88', '8 8')

data = data.split()
print(len(max(data, key=len)))