with open ('17_17636 (1).txt') as file:
    data = [int(i) for i in file]

maxx = max([i for i in data if str(i)[-1] == '3' and len(str(abs(i))) == 3])

ans = []
for i in range(len(data)-2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    u1 = (str(num1)[-1] == '3') and (len(str(abs(num1))) == 3)
    u2 = str(num2)[-1] == '3' and len(str(abs(num2))) == 3
    u3 = str(num3)[-1] == '3' and len(str(abs(num3))) == 3
    if u1 + u2 + u3 >= 1:
        if num1 + num2 + num3 < maxx:
            ans.append(num1 + num2 + num3)

print(len(ans), max(ans))