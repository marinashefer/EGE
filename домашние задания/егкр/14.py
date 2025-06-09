def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 3001):
    num = 4**210 + 4**110 - x
    num4 = convert(num, 4)
    ans.append([num4.count('0'), x])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))
print(ans)
print(ans[0])