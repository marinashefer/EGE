from itertools import *

cnt = 0
for val in product('01234567', repeat=6):
    val = ''.join(val)
    if val[0] != '0':
        if int(val, 8) % 5 == 0:
            if len(val) == len(set(val)):
                val = val.replace('3', '1').replace('5', '1').replace('7', '1')
                if '11' not in val:
                    val = val.replace('2', '0').replace('4', '0').replace('6', '0')
                    if '00' not in val:
                        cnt += 1

print(cnt)