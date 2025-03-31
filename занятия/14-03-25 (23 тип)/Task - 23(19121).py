def f(cur, end):
    if cur == end:
        return 1
    if cur < end:
        return 0
    return f(cur - 3, end) + f(cur // 3, end)

print(f(35, 8) * f(8, 1))