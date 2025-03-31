def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

a = []
for n in range(0, 10000):
    r = conv(n, 3)
    if (r.count('1') + r.count('2')) % 3 == 0:
        r ='20' + r
    else:
        r = '10' + r

    if int(r, 3) < 100:
        a.append(n)

print(max(a))

