def f(cur, end, cnt=0):
    if cur % 2 == 0:
        cnt += 1
    if cur == end and cnt <= 15:
        return 1
    if cur > end:
        return 0
    return f(cur + 2, end, cnt) + f(cur + 3, end, cnt) + f(cur * 2 + 1, end, cnt)

print(f(1, 55))