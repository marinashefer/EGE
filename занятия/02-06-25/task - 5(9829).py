def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1,1000):
    r = convert(n, 3)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + convert((n % 3) * 4, 3)

    if int(r, 3) < 199:
        ans.append(n)

print(max(ans))