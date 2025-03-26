def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 1000):
    r = convert(n, 4)
    if sum(map(int, r)) % 2 == 0:
        r = r + r[-2:]
    else:
        r = '2' + r + '0'

    if int(r, 4) > 120 and int(r, 4) % 2 == 0:
        ans.append(int(r, 4))

print(min(ans))