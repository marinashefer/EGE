def f(cur, end):
    ans = []
    if cur == end and (len(ans) == len(set(ans))):
        return 1
    if cur > 50 or cur < (-50):
        return 0
    ans.append(cur)
    return f(cur + 2, end) + f(cur - 3, end)

print(f(1, 30))