with open ('24_19254.txt') as file:
    data = file.readline()

data = data.split('FSRQ')
ans = []

for i in range(len(data)-80):
    s = 'FSRQ'.join(data[i:i+81])
    ans.append(len(s))

print(max(ans)+6)