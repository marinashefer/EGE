with open ('24_17535.txt') as file:
    data = file.readline()

data = data.split('CD')

ans = 0
for i in range(len(data)-160):
    st = 'CD'.join(data[i:i+161])
    ans = max(ans, len(st))

print(ans + 2) # (+2) обязательно! так как CD