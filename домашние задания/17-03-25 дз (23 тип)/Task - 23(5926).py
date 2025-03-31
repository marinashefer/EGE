def f(cur, cnt=0, first=0, second=0, third=0):
    if cnt == 24:
        return 1
    if cnt == 0:
        return f(cur + 1, cnt + 1, 1, 0, 0) + f(cur + 7, cnt + 1, 0, 1, 0) + f(cur * 4, cnt + 1, 0, 0, 1)
    if first == 1:
        return f(cur + 7, cnt + 1, 0, 1, 0) + f(cur * 4, cnt + 1, 0, 0, 1)
    if second == 1:
        return f(cur + 1, cnt + 1, 1, 0, 0) + f(cur * 4, cnt + 1, 0, 0, 1)
    if third == 1:
        return f(cur + 1, cnt + 1, 1, 0, 0) + f(cur + 7, cnt + 1, 0, 1, 0)

print(f(1))