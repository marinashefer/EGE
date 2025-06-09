def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(3, 10000):
    r = convert(n, 3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + convert(((n % 3)*3), 3)

    if int(r, 3) <= 150:
        ans.append(n)

print(max(ans))
