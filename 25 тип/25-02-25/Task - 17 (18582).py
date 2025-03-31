with open ('17.txt') as file:
    data = [int(i) for i in file]

minn = min([int(i) for i in data])

ans = []
for i in range(len(data)-2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    otr = []
    pol = []
    if num1 < 0:
        otr.append(num1)
    else:
        pol.append(num1)
    if num2 < 0:
        otr.append(num2)
    else:
        pol.append(num2)
    if num3 < 0:
        otr.append(num3)
    else:
        pol.append(num3)
    if len(otr) > len(pol):
        if str(num1 + num2 + num3)[-1] == str(minn)[-1]:
            ans.append(abs(num1 + num2 + num3))

print(len(ans), max(ans))
