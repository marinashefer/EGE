def f(cur, end):
    if cur == end:
        return 1
    if cur > end or cur == 56:
        return 0
    return f(cur+3, end) + f(cur+7, end) + f(cur*3, end)

print(f(12, 40) * f(40, 72) * f(72, 89))