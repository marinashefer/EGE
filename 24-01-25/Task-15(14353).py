def f(A):
    for x in range(1, 1000):
        f = (((A + 7 > x) and (7 + x > A) and (x + A > 7)) <= (((max(x+5, 14)) <= 27)) == (not((36+21 > x) and (36+x > 21) and (x+21 > 36))))
        if not f:
            return False
    return True

ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)

print(max(ans))