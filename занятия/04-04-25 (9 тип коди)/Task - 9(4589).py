from itertools import *

def f1(arr):
    return max(arr) < sum(arr) - max(arr)

def f2(arr):
    return max(arr) + min(arr) == sum(arr) - max(arr) - min(arr)

def f3(arr):
    for i in permutations(arr):
        if sum(i[2:]) == sum(i[:2]):
            return True
    return False

def f4(arr):
    for i in combinations(arr, 2):
        if sum(i) == sum(arr) - sum(i):
            return True
    return False

with open ('9_4589.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i) and f3(i) and f4(i):
        cnt += 1

print(cnt)