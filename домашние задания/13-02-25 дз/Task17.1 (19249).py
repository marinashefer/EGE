with open ('17.1.txt') as file:
    data = [int(i) for i in file]

ans = []
max_num = max(i for i in data if 10000 <= abs(i) <= 99999 and str(i)[-2:] == '43')

for i in range(len(data) - 2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]

    u1 = 10000 <= abs(num1) <= 99999
    u2 = 10000 <= abs(num2) <= 99999
    u3 = 10000 <= abs(num3) <= 99999

    p1 = str(num1)[-2:] == '43'
    p2 = str(num2)[-2:] == '43'
    p3 = str(num3)[-2:] == '43'

    f1 = (u1 and p1) + (u2 and p2) + (u3 and p3) >= 1
    f2 = num1**2 + num2**2 + num3**2 <= max_num** 2

    if f1 and f2:
        ans.append(num1**2 + num2**2 + num3**2)

print(len(ans), min(ans))