from itertools import permutations

graph = 'AB AH BH HF FD FG CD CG GE EC EA'.split()
matrix = '247 148 578 126 38 47 136 236'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)