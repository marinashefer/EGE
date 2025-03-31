def f(cur, end):
    if cur > end or cur == 17:
        return 0
    if cur == end:
        return 1
    return f(cur + 1, end) + f(cur * 2, end)

print(f(1, 10) * f(10, 35))