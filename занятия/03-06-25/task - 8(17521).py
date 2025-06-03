from itertools import *

cnt = 0
for val in product('01234567', repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val[0] in '246':
            if val[-1] not in '26':
                if val.count('7') <= 2:
                    cnt += 1

print(cnt)