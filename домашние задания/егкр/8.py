from itertools import *

alph = sorted('ПОБЕДА')

ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] == 'О':
        if pos % 2 == 0:
            if len(val) == len(set(val)):
                ans.append([pos, val])

print(max(ans))