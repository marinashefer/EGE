with open ('17.3.txt') as file:
    data = [int(i) for i in file]

max_num = max(i for i in data if str(i)[-1] == '3')
ans = []

for i in range(len(data) - 1):
    num1, num2 = data[i], data[i+1]
    u1 = str(num1)[-1] == '3'
    u2 = str(num2)[-1] == '3'
    f1 = u1 + u2 == 1
    f2 = num1**2 + num2**2 >= max_num**2
    if f1 and f2:
        ans.append(num1**2 + num2**2)

print(len(ans), max(ans))