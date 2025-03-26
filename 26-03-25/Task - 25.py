def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)

    if len(res) <= 2:
        m = 0
    else:
        m = max(res) - min(res)

    if str(m)[-1] == '6':
        return m

cnt = 0
for i in range(300001, 10**20):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break



