from itertools import product

cnt = 0
for val in product('КОТБУС', repeat=8):
    val = ''.join(val)
    gl = 'ОУ'
    if 'КОТ' in val and val[0] not in gl:
        cnt += 1

print(cnt)