def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2031):
    num = 3**100 - x
    num3 = convert(num, 3)
    if num3.count('0') == 1:
        ans.append([x, num3])

print(max(ans))