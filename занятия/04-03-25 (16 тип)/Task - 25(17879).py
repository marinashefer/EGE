def f(num):
    res = set()
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            res |= {i, num // i}
    res =sorted(res)

    if len(res) <= 1:
        return 0
    m = min(res) + max(res)
    return m

cnt = 0
for i in range(800001, 10**20):
    if f(i) % 10 == 4:
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break