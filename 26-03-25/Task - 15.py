def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x+2 <= 50) or (y < x+10) or (x >= a)
            if not f:
                return False
    return True

ans = []
for a in range(1, 1000):
    if f(a):
        ans.append(a)

print(max(ans))
