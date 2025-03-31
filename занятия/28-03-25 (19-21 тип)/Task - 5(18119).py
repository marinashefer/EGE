def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 1000):
    r = convert(n, 3)
    if sum(map(int, r)) % 2 == 0:
        r = '1' + r + '2'
    else:
        r = '2' + r + '0'

    if int(r, 3) > 100:
        ans.append(int(r, 3))

print(min(ans))





