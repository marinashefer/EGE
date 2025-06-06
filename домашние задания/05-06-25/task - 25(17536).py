def f(num):
    ans = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            ans += [i, num//i]
    ans = sorted(set(ans))

    if len(ans) < 2:
        m = 0
    else:
        m = min(ans) + max(ans)

    if str(m)[-1] == '4':
        return m
    else:
        return 0

cnt = 0
for i in range(800001, 10**10):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt ==5:
            break








