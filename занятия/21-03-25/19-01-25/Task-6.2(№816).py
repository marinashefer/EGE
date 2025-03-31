# print('x y z')
#
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             f = (not (x == (y <= z)))
#             print(x, y, z, f)

from itertools import permutations

def f(x, y, z):
    return (not(x == (y <= z)))

table =[(0, 0, 1), (0, 1, 1)]
for p in permutations('xyz'):
    u = [f(**dict(zip(p, t))) for t in table] == [1, 0]
    if u:
        print(*p)