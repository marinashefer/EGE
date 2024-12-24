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
        summ = r.count('1') + r.count('2')*2
        r = r + convert(summ, 3)
    if int(r, 3) % 2 == 0 and int(r, 3) > 220:
        ans.append(int(r, 3))

print(min(ans))
