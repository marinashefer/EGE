def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 8)
    if n % 2 == 0:
        r = r + max(r)
    else:
        r = r + min(r)*2
    if int(r, 8) < 313:
        ans.append(n)

print(max(ans))
