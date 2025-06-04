def f(x):
    for x in range(1, 10000):
        f = (x % a == 0) or ((60 <= x <=  80) <= (not(x % 22 == 0)))
        if not f:
            return False
    return True

for a in range(1, 10000)[::-1]:
    if f(a):
        print(a)
        break