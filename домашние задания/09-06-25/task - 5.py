def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(10, 10**8):
    r = convert(n, 3)
    r = r.replace('0', '*')
    r = r.replace('*', '2')
    r = r.replace('2', '0')
    r = r.lstrip('0')
    print(r)

    r = int(r, 3)
    ans1 = abs(n - r)
    if ans1 == 1864246:
        print(n)
        break
