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
        if num % i == 0 and is_prime(i):
            res |= {i}
            if num % (num // i) == 0 and is_prime(num // i):
                res |= {num // i}
        elif num % (num//i) == 0 and is_prime(num//i):
            res |= {num//i}
    res = sorted(res)

    summ = sum(res)
    if len(res) == 0:
        return 0
    return summ

cnt = 0
for i in range(32500001, 10**30):
    if f(i) != 0:
        if f(i) % 145 == 0:
            print(i, f(i))
            cnt += 1
            if cnt == 7:
                break














