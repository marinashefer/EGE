from itertools import *

def f(x, y, w, z):
    return (w <= (y == z)) and (y == (z <= x))

for a1, a2 in product([0, 1], repeat=2):
    table = [(a1, 0, 0, 0), (0, a2, 1, 1), (0, 0, 0, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 0]:
                print(*p)