def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(2, 2026):
    num = 5**2025 + 5**200 - x
    num_5 = convert(num, 5)
    ans.append([num_5.count('4'), x])

print(max(ans))