from itertools import product

alph = '0123456789ABCD'

cnt = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('0') == 2:
            if sum([val.count(i) for i in 'ABCD']) <= 4:
                cnt += 1

print(cnt)