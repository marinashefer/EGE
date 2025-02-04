def convert(num, sys):
    alph = '0123456789AB'
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res [::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 12)
    if n % 3 == 0:
        r = '1' + r + 'B'
    else:
        r = '2' + r + '0'
    if int(r, 12) < 1996:
        ans.append(int(r, 12))

print(max(ans))








