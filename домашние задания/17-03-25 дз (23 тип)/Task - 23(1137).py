def f(cur, end):
    if cur == end:
        return 1
    if cur > end:
        return 0
    return f(cur+1, end) + f(int(str(cur)+'0'), end) + f(int(str(cur)+'1'), end)

print(f(100, 11101))