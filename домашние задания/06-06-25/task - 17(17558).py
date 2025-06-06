with open ('17_17558.txt') as file:
    data = [int(i) for i in file]

cnt = len([i for i in data if abs(i) % 32 == 0])

ans = []
for i in range(len(data)-1):
    num1, num2 = data[i], data[i+1]
    u1 = num1 < 0
    u2 = num2 < 0
    if u1 + u2 >= 1:
        if num1 + num2 < cnt:
            ans.append(num1+num2)

print(len(ans), max(ans))