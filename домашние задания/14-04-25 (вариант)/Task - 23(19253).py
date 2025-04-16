def f(cur, end):
    if cur == end: return 1
    if cur < end or cur == 24: return 0
    return f(cur - 1, end) + f(cur - 6, end) + f(cur // 2, end)

print(f(34, 29) * f(29, 19) * f(19, 6))