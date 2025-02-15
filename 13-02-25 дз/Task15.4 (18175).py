def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = ((not(x % 7 == 0)) and (x % 13 == 0)) <= (x > a - 40)
            if not f:
                return False
    return True

ans = []
for a in range(1, 10000):
    if f(a):
        ans.append(a)

print(max(ans))