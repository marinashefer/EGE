from itertools import *

cnt = 0
for val in product('012345678', repeat=7):
    val = ''.join(val)
    if val[0] in '2468':
        if int(val[-1]) % 3 != 0:
            if val.count('6') >= 1:
                cnt += 1
print(cnt)
