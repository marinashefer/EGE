def f(x1, x2, s):
    if x1 + x2 <= 72: return s % 2 == 0
    if s == 0: return 0
    h = [f(x1-3, x2, s-1),
         f(x1, x2-3, s-1),
         f(x1//2 if x1 % 2 == 0 else (x1//2)+1, x2, s-1),
         f(x1, x2//2 if x2 % 2 == 0 else (x2//2)+1, s-1)]
    return any(h) if (s-1) % 2 == 0 else any(h)

print('19)', [s for s in range(23, 1000) if f(50, s, 2)])
print('20)', [s for s in range(23, 1000) if f(50, s, 3) and not f(50, s, 1)])
print('21)', [s for s in range(23, 1000) if f(50, s, 4) and not f(50, s, 2)])







