from functools import lru_cache

@lru_cache(None)

cnt = 0
def f(n):
    if n <= 2:
        cnt += 1
        return 2
    if n > 2:
        return (f(n-1) - 2) * f(n-2)
        cnt += 1

for i in range(60):
    f(i)

print(f(57))