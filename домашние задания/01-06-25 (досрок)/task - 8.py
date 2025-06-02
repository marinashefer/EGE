from itertools import *

alph = sorted('ДГИАШЭ')
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] not in 'ИАЭ':
        if val[-1] not in 'ДГШ':
            cnt += 1

print(cnt)