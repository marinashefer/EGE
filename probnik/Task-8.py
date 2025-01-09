from itertools import product

cnt = 0
for val in product('ABCDEF', repeat=6):
    val = ''.join(val)
    if val[0] in 'BCDF':
        if val[-1] in 'BCDF':
            cnt += 1

print(cnt)