def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 5556):
    num = 5**150 + 5**135 - x
    num5 = convert(num, 5)
    if num5.count('4') == 134:
        ans.append(x)

print(max(ans))