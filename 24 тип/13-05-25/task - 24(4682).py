with open ('24_4682.txt') as file:
    data = file.readline()

data = data.replace('A', 'E')

for i in 'BCD':
    data = data.replace(i, 'D')

data = data.replace('DE', '*')

for i in 'ABCDE':
    data = data.replace(i, ' ')
    
data = data.split()

print(len(max(data, key=len)))