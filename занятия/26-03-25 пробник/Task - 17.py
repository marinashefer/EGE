with open ('17.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if str(i)[-2:] == '19' and len(str(abs(i))) == 3)

ans = []
for i in range(len(data)-2):
    num1 = data[i]
    num2 = data[i+1]
    num3 = data[i+2]
    u1 = str(num1)[-2:] == '19' and len(str(abs(num1))) == 5
    u2 = str(num2)[-2:] == '19' and len(str(abs(num2))) == 5
    u3 = str(num3)[-2:] == '19' and len(str(abs(num3))) == 5
    if u1 + u2 + u3 >= 1:
        if (num1 + num2 + num3) > (minn**2):
            ans.append(num1 + num2 + num3)

print(len(ans), min(ans))