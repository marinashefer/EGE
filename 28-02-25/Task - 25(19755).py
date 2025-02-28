def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i): res.add(i)
            if is_prime(num // i): res.add(num //i)
    if len(res) <= 1:
        return 0
    m = min(res) + max(res)
    if m > 2000 and m % 10 == 8:
        return m
    return 0

cnt = 0
for i in range(1200001, 10**20):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break
