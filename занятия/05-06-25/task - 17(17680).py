with open ('17_17680.txt') as file:
    data = [int(i) for i in file]

minn =  min([i for i in data if i > 0 and abs(i) % 41 == 0])

ans = []
for i in range(len(data)-1):
    num1, num2 = data[i], data[i+1]
    if num1 != num2:
        if abs(num1 - num2) % minn == 0:
            ans.append(num1+num2)

print(len(ans), max(ans))