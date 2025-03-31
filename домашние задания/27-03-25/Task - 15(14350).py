def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (not((x < 7) or (y >= (3*x + a - 20)) or (x >= 34) or (y < 121)))
            if f:
                return False
    return True

ans = []
for i in range(0, 1000):
    if f(i):
        ans.append(i)

print(max(ans))