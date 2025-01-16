def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(10, 10000):
    r = convert(n, 3)
    if (r.count('2') + r.count('0')) > r.count('1'):
        r = '22' + r
    else:
        r = '11' + r
    if int(r, 3) > 100:
        ans.append(int(r, 3))

print(min(ans))