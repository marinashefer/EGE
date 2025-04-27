from string import digits, ascii_lowercase

with open ('17_2399.txt') as file:
    data = [int(i) for i in file]

sum_35 = sum(data) // 35

def convert(num, sys):
    alph = digits + ascii_lowercase[:16]
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

ans = []
for i in range(len(data)-1):
    num1 = data[i]
    num2 = data[i+1]
    u1 = num1 > sum_35
    u2 = num2 > sum_35
    if u1 + u2 == 1:
        if u1:
            if convert(num2, 16)[:-2] == 'ef':
                ans.append(num1 + num2)
        if u2:
            if convert(num1, 16)[:-2] == 'ef':
                ans.append(num1 + num2)

print(len(ans), min(ans))