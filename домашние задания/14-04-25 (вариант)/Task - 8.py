from itertools import *

cnt = 0
for val in product('01234', repeat=6):
    val = ''.join(val)
    if val[0] == '3':
        if sum(map(int, val)) % 2 == 0:
            cnt += 1

print(cnt)