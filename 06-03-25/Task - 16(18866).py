from functools import lru_cache

@lru_cache(None)

def f(n):
    if n < 100:
        return n**2
    if n > 99 and n % 2 == 0:
        return 0.5 * f(n - 1)
    if n > 99 and n % 2 == 1:
        return 2 * f(n -1)

for i in range(1, 17000):
    f(i)

print(1000 * f(16384) // f(7777))