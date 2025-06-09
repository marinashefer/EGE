with open ('24_10105.txt') as file:
    data = file.readline()

data = data.split('T')
ans = []
for i in range(len(data)-100):
    s = 'T'.join(data[i:i+101])
    ans.append(len(s))

print(max(ans))

