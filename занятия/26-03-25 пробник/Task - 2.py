from itertools import product, permutations

def f(x, y, w, z):
    return x and ((z <= y) == w)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(1, a1, 1, a2), (0, a3, 1, 1), (1, 1, 1, a4), (1, 1, 1, a5)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1, 1]:
                print(*p)