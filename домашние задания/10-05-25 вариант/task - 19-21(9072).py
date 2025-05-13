def f(x, s):
    if x >= 100: return s % 2 == 0
    if s == 0: return 0
    h = [f(x+7, s-1),
         f(x*2, s-1)]
    return any(h) if (s-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 100) if f(2, s)])
print('20)', [s for s in range(1, 100) if f(3, s)])
print('21)', [s for s in range(1, 100) if f(4, s) and not f(2, s)])