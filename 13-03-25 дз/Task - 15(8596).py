def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x >= 11) or (3 * x < y) or (x * y < a)
            if not f:
                return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
        break

