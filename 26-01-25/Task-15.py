def f(A):
    for x in range(0, 10000):
        for y in range(0, 10000):
            f = (not((x * y) > A+13)) <= (((28 * y) > 520) or ((x * 25) > 800))
            if not f:
                return False
    return True

ans = []
for A in range(0, 100000):
    if f(A):
        ans.append(A)

print(max(ans))