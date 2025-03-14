with open ('17.txt') as file:
    data = [int(i) for i in file]

max_l = max([i for i in data if str(i)[-3:] == '121'])

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    cnt = 0
    if 1000 <= abs(num1) <= 9999 and num1 % 2== 0:
        cnt += 1
    if 1000 <= abs(num2) <= 9999 and num2 % 2== 0:
        cnt += 1
    if 1000 <= abs(num3) <= 9999 and num3 % 2== 0:
        cnt += 1
    if cnt <= 1:
        if num1 + num2 + num3 <= max_l:
            ans.append(num1 + num2 + num3)

print(len(ans), max(ans))










