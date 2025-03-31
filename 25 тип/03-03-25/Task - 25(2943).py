def f(num):
    res = set()
    for i in range(2 , int(num ** 0.5)+1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(set(res))

    if len(res) <= 1:
        m = 0
    else:
        m = min(res) + max(res)

    cnt = 0
    for i in range(220000, 10**20):
        if m % 10 == 4:
            print(i, m)
            cnt += 1
            if m == 5:
                break