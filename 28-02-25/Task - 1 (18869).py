from itertools import permutations

graph = 'EH HA AB BC CD DE EF HG GF FC GA'.split()
matrix = '568 36 247 368 178 124 35 145'.split()

print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)












