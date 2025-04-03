def f(num):
    res = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res.append(i)
            res.append(num//i)
    res = sorted(set(res), reverse=True)

    if len(res) >= 7:
        return res[6], len(res)
    return False

cnt = 0
for i in range(400000001, 40000000100000):
    if f(i):
        print(f(i))
        cnt += 1
        if cnt == 5:
            break