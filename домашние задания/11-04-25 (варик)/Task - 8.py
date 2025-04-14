from itertools import *

alph = sorted('ЛОДКА')

cnt = 0
for pos, val in enumerate(product(alph, repeat=4), 0):
    val = ''.join(val)
    if val.count('O') >= 2:
        cnt += 1

print(cnt)