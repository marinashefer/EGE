def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 and i % 2 == 1:
            res |= {i, num//i}
    res = sorted(res, reverse=False)

    if len(res) < 6:
        return 0
    else:
        return res[5]

cnt = 0
for i in range(200001, 10**20):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break