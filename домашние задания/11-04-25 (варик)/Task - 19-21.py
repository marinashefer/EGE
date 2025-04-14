def f(x1, x2, s):
    if x1 + x2 >= 49: return s % 2 == 0
    if s == 0: return False
    h = [f(x1+1, x2, s-1), f(x1, x2+1, s-1), f(x1*3, x2, s-1), f(x1, x2*3, s-1)]
    return any(h) if (s-1) % 2 == 0 else any(h)

print('19', [s for s in range(1, 44) if f(5, s, 2)])