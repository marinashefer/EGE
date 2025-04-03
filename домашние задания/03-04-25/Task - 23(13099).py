def f(cur, end, cnt_a=0):
    if cur == end:
        return 1
    if cur-1 > end:
        return 0
    if cnt_a == 1:
        return f(cur * 2, end, 0) + f(cur * 3, end, 0)
    return f(cur-1, end, 1) + f(cur*2, end, 0) + f(cur*3, end, 0)

print(f(3, 15))