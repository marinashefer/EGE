from itertools import permutations

graph = 'АБ БГ ГД ДЕ ЕК КВ ВА БД ВЕ'.split()
matrix = '47 56 46 137 267 235 145'.split()

print(*range(1, 8))

for i in permutations('АБВГДЕК'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)