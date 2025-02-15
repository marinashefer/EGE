from itertools import product

cnt = 0
alph = sorted('ЯСНОВИДЕЦ')

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] in 'СНВДЦ' and val[-1] in 'ЯОИЕ':
        if (val.count(val[0]) == 1) and (val.count(val[-1]) == 1):
            cnt += 1

print(cnt)