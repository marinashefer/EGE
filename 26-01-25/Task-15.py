def f(A):
    for x in range(1, 1000):
        for y in range(1, 10000):
            f = (not((x * y) > A+13)) <= (((28 * y) > 520) or ((x * 25) > 800))
            if not f:
                return False
    return True


for A in range(-30, 100):
    if f(A):
        print(A)