def f(A):
    for x in range(1, 10000):
        f = ((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (A <= x)
        if not f:
            return False
    return True

ans = []
for A in range(0,10000):
    if f(A):
        ans.append(A)

print(max(ans))