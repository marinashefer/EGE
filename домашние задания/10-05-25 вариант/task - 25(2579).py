def f(num):
    res = set()
    if num < 2:
        return 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)

    if len(res) < 3:
        return 0
    return res[-1] + res[-2] + res[-3]

cnt = 0
for i in range(10000001, 10**20):
    if f(i):
        if f(i) == 0:
            break
        if (f(i)**0.5) * int(f(i)**0.5) == f(i):
            cnt += 1
            print(f(i))
            if cnt == 5:
                break
