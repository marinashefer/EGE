with open ('17.5.txt') as file:
    data = [int(i) for i in file]

s = set(data)
cnt = 0
moda = 0
for i in s:
    if cnt < data.count(i):
        cnt = data.count(i)
        moda = i

ans = []
for i in range(len(data)):
    for j in range(i+2, len(data), 2):
        if data[i] < moda < data[j] or data[j] < moda < data[i]:
            ans.append(max(abs(moda - data[i]), abs(moda - data[j])))

s = [data.count(i) for i in range(-1000, 1001)]
moda = s.index(max(s)) - 1000

print(len(ans), max(ans))