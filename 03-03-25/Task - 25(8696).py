def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)

    if len(res) <= 1:
        return 0
    else:
        m = sum(res)

    if is_prime(m % 100000):
        return m
    return 0

cnt = 0
for i in range(1273548, 10**20):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break







