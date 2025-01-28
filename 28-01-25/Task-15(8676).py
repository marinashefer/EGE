def f(B):
    for x in range(0, 10000):
        f = ((x & 500 != 0) and (x & 200 == 0)) <= (not(x & B == 0))
        if not f:
            return False
    return True

for B in range(0, 10000):
    if f(B):
        print(B)
        break

