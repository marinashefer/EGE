def f(A):
    for x in range(1, 1000):
        f = (A % x == 0) <= ((x == A) or (x == 1))
        if not f:
            return False
    return True

ans = []
for A in range(1, 11112):
    if f(A):
        ans.append(A)

print(len(ans))