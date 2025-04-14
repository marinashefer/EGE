from itertools import permutations

graph = 'CG GE ED EA DA BD AF BF CF'.split()
matrix = '23 145 16 27 267 357 456'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)