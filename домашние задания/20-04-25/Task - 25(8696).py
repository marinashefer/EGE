def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res |= {i, num//i}
    return sum(res)

cnt = 0
for i in range(1273548, 10**10):
    if is_prime(f(i) % 100000):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break



