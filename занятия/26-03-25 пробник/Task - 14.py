def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2031):
    num = 2**2023 + 2**2024 - 2**2021 - x
    num2 = convert(num, 4)
    ans.append([num2.count('0'), x])

ans = sorted(ans, reverse=True)
print(ans)