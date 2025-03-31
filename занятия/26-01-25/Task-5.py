def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + convert((n % 3) * 5, 3)

    if int(r, 3) >  133:
        ans.append(int(r, 3))

print(min(ans))