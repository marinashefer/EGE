with open ('17_21712.txt') as file:
    data = [int(i) for i in file]

minn = min([i for i in data if i > 0 and len(str(abs(i))) == 4 and str(i)[-1] == '6'])

ans = []
for i in range(len(data)-2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    u1 = len(str(abs(num1))) == 4 and str(num1)[-1] == '6'
    u2 = len(str(abs(num2))) == 4 and str(num2)[-1] == '6'
    u3 = len(str(abs(num3))) == 4 and str(num3)[-1] == '6'
    if u1 + u2 + u3 == 1:
        if num1 + num2 + num3 <= minn:
            ans.append(num1+num2+num3)

print(len(ans), max(ans))

