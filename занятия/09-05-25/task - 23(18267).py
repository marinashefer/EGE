def f(cur, end, n):
    if cur == end and n == 0:
        return 1
    if cur > end:
        return 0
    return f(cur + 2, end, 0) + f(cur + 5, end, 0) + f(cur ** 2, end, 1)

print(f(4, 36, 0))