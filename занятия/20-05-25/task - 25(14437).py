def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}

    if len(res) != 0:
        m = sum(res) // len(res)
        if str(m)[-3:] == '313':
            return m
    else:
        return 0

cnt = 0
for i in range(1, 700000)[::-1]:
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 7:
            break