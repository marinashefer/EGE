def deliteli(num):
    ans = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            ans += [i, num//i]
    ans = set(ans)

    r = sum(ans)
    if str(r)[-1] == '6':
        return r
    else:
        return False

cnt = 0
for i in range(500001, 10**10):
    f = deliteli(i)
    if f:
        print(i, f)
        cnt += 1
        if cnt == 5:
            break