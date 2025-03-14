def f(cur, end, A=0):
    if cur == end:
        return 1
    if cur > end + 1:
        return 0
    if A == 0:
        return f(cur - 1, end, 1) + f(cur * 2, end) + f(cur * 3, end)
    return f(cur * 2, end) + f(cur * 3, end)

print(f(3, 15))