from string import digits, ascii_lowercase

def convert(num, sys):
    alph = digits + ascii_lowercase[:16]
    res = ''
    while num:
        res += alph[num%sys]
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 1000):
    r = convert(n, 16)
    if r.count('b') % 2 == 0:
        r = '1' + r
    else:
        r = r + '1'

    if 10 <= int(r, 16) <= 99:
        ans.append(n)

print(len(ans))
