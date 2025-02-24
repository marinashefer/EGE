with open ('17.txt') as file:
    data = [int(i) for i in file]

max_50 = max([int(i) for i in data if str(i)[-2:] == '50'])
print(max_50)

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    if (num1 != num2) and (num1 != num3) and (num2 != num3):
        if (10000 <= abs(num1) <= 99999) and (10000 <= abs(num2) <= 99999) and (10000 <= abs(num3) <= 99999):
            if (num1 + num2 + num3) <= max_50:
                ans.append(num1 + num2 + num3)

print(len(ans), max(ans))