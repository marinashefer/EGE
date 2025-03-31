def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res [::-1]

ans = []
for n in range(1, 100):
    r = convert(n, 4)
    cnt = 0
    for i in range(0, len(r)):
        while r[i] == 0:
            cnt += 1
            i += 1
        break

    znach = len(r) - cnt

    if znach % 2 == 0:
        r = r[:len(r)//2] + '0' + r[len(r)//2]
    else:
        r = r

    if int(r, 4) < 180:
        ans.append(n)

print(max(ans))