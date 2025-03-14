def f(cur, end, a=0, b=0, c=0):
    if cur == end and a <= 4 and b >= 2 and c == 5:
        return 1
    if cur > end:
        return 0
    return f(cur * 5, end, a + 1, b, c) + f(cur * 3, end, a, b + 1, c) + f(cur + 45, end, a, b, c +1)

print(f(1, 2970))