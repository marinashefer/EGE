def f(cur, end):
    if cur > end or cur == 11:
        return 0
    if cur == end:
        return 1
    return f(cur + 1, end) + f(cur * 2, end) + f(cur * cur, end)

print(f(2, 20))