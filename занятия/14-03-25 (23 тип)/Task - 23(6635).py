def f(cur , cnt=0):
    if cnt == 13 and cur < 0:
        return [cur]
    if cnt > 13:
        return []
    return f(cur - 3, cnt + 1) + f(cur * (-3), cnt + 1)

print(len(set(f(333))))