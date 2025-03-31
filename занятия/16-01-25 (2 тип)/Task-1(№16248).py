from itertools import permutations

graph = 'AB BC CA AD DF FG CE EG EF DC ED'.split()
matrix = '347 3456 1245 1238 237 25 14'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)