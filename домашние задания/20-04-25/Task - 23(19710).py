from sys import setrecursionlimit

def f(cur, end):
    if cur == end: return 1
    if cur > end or cur == 8: return 0
    return f(cur+3, end) + f(cur*2, end)

setrecursionlimit(1000)

print(f(2, 32) * f(32, 76))