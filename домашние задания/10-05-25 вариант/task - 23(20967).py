def f(cur, end):
    if cur == end: return 1
    if cur < end or cur == 15: return 0
    return f(cur-2, end) + f(cur-3, end) + f(cur // 3, end)

print(f(48, 25) * f(25, 17) * f(17, 4))