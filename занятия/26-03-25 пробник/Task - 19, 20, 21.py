def f(x1, x2, c, win):
    if x1 + x2 >= 127:
        return c in win
    if c > max(win):
        return 0
    moves = [f(x1+2, x2, c+1, win), f(x1, x2+2, c+1, win), f(x1*3, x2, c+1, win), f(x1, x2*3, c+1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return any(moves)

for s in range(1, 123):
    if f(2, s, 0, [2]) == 1:
        print('19)', s)


