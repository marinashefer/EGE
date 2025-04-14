def f(cur, end, n=0):
    if cur > end: return 0
    if cur == end: return 1
    return f(cur+1, end, n+1) + f(cur +2, end, n+1) + f(cur*2, end, n+1)

print(f(1, end, 7))