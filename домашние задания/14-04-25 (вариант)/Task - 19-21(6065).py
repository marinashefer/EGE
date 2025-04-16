def f(x, s, c=0):
    if x > 40: return s % 2 == 0
    if s == 0: return 0
    h = [f(x+3, s-1, 1),
         f(x+6, s-1, 2),
         f(x*2, s-1, 3)]
    if c == 1:
        h = [f(x+6, s-1, 2),
         f(x*2, s-1, 3)]
    if c == 2:
        h = [f(x+3, s-1, 1),
         f(x*2, s-1, 3)]
    if c == 3:
        h = [f(x+6, s-1, 2),
         f(x+3, s-1, 1)]
    return any(h) if (s-1) % 2 == 0 else all(h)

print('19:', [s for s in range(2, 37) if f(s, 2)])
print('20:', [s for s in range(2, 37) if not f(s, 1) and f(s, 3)])
print('21:', [s for s in range(2, 37) if f(s, 4) and not f(s, 2)])

