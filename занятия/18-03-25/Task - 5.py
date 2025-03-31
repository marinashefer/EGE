from string import digits, ascii_lowercase

ans = []
def convert(num, sys):
    alph = digits + ascii_lowercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

for n in range(1, 10000):
    r = convert(n, 12)
    if n % 3 == 0:
        r = '1' + r + 'B'
    else:
        r = '2' + r + '0'

    if int(r, 12) < 1996:
        ans.append(int(r, 12))

print(max(ans))











