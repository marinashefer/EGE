with open ('17-1.txt') as file:
    data = [int(i) for i in file]

chislo_7 = [int(i) for i in data if str(i)[-1] == '7']

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i], data[i+1]
    if (num1 > 0 and num2 < 0 ) or (num2 > 0 and num1 < 0 ):
        if num1 + num2 < len(chislo_7):
            ans.append(num1+num2)

print(len(ans), max(ans))