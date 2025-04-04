from itertools import *

ans = []
alph = sorted('АРГУМЕНТ')
for pos, val in enumerate(product(alph, repeat=4), 1):
    val = ''.join(val)
    if len(val) == len(set(val)):
        if list(val) == sorted(val):
            ans.append([pos, val])

print(max(ans))









