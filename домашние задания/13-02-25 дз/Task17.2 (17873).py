with open ('17.2.txt') as file:
    data = [int(i) for i in file]

min_num = min(i for i in data)
ans = []

for i in range(len(data) - 1):
    num1, num2 = data[i], data[i+1]
    u1 = num1 % 16 == min_num
    u2 = num2 % 16 == min_num
    if u1 + u2 >= 1:
        ans.append(num1+num2)

print(len(ans), max(ans))