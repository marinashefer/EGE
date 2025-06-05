with open ('17_17873.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans = []
for i in range(len(data)-1):
    num1, num2 = data[i], data[i+1]
    u1 = num1 % 16 == minn
    u2 = num2 % 16 == minn
    if u1 + u2 >= 1:
        ans.append(num1+num2)

print(len(ans), max(ans))