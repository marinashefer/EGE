from itertools import *
from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

cnt = 0
for val in product(alph[:15], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('8') == 1:
            if len([i for i in val if i not in '0123456789']) >= 2:
                cnt += 1

print(cnt)