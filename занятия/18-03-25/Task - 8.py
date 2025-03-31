from string import digits, ascii_lowercase
from itertools import *

cnt = 0
alph = digits + ascii_lowercase
for val in product(alph[:12], repeat=5):
    val = ''.join(val)
    if val.count('7') == 1 and val[0] != '0':
        val = val.replace('a', '9').replace('b', '9')
        if val.count('9') <= 3:
            cnt += 1

print(cnt)
