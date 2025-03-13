def f(a):
    for x in range(1, 1000):
        f = ((x & 52 != 0) and (x & 36 == 0)) <= (not (x & a == 0))
        if not f:
            return False
    return True

for i in range(1, 1000):
    if f(i):
        print(i)
        break