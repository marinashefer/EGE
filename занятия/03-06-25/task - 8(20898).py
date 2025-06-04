from itertools import *

cnt = 0
for val in  product('012345678', repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('0') == 1:
            val = val.replace('3', '1').replace('5', '1').replace('7', '1')
            if '01' not in val and '10' not in val:
                cnt += 1

print(cnt)