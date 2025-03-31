def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)

    if len(res) == 0:
        m = 0
    m = sum(res)

    if is_prime(m % 100000):
        return m

cnt = 0
for i in range(1273547, 10**30):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break



