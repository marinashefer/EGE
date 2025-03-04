def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 1000):
    r = convert(n, 7)
    if n % 2 == 0:
        r = '52' + r + '1'
    else:
        r = r[-1] + r[1:-1] + r[0] + '15'

    cnt = 0
    for i in range(0, len(r)):
        if r[i] == '0':
            cnt += 1
        else:
            break
    #r = r.strip('0')

    if len(r) - cnt == 4:
        ans.append(n)

print(max(ans))









