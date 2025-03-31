def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(set(res))

    if len(res) <= 1:
        return 0

    m = min(res) + max(res)
    if m % 10 == 4:
        return m

cnt = 0
for i in range(700001, 10**20):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break