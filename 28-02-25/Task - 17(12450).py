with open ('17.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i % 52 == 0)

ans =[]

for i in range(len(data) - 2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    if (num1 % 113) + (num2 % 113) + (num3 % 113) == minn:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))
