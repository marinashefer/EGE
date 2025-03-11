def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(set(res))

for i in range(1273547, 10**20):
    deliteli = [f(i)]
    print(deliteli)
    if is_prime(num):
        m = 0
    else:
        m = sum(i for i in deliteli)
    if m % 100000 == is_prime(num):
        print(num, m)










