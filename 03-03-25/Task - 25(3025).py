def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if i % 2 == 0:
            res |= {i, num // i}
    res = sorted(set(res))
    if len(res) < 6:
        d = 0
    else:
        d = res[5]

cnt = 0
for i in range(200_000_000, 20**20):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break
