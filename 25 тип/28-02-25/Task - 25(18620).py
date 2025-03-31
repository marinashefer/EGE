def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(set(res))

    m = res[-1] + res[-2]
    if str(m)[-4:] == '1214':
        return m
    if len(res) < 2:
        m = 0

for i in range(112500000, 112550001):
    if f(i):
        print(i)

# https://kompege.ru/variant?kim=25085301