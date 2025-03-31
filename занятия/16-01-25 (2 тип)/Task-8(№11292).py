from itertools import product
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

cnt = 0
for val in product(alph[:16], repeat=5):
    val = ''.join(val)
    if val.count('6') == 2 and val[0] != '0' and 'A6' not in val and '6A' not in val and 'C6' not in val and '6C' not in val and '6E' not in val and 'E6' not in val and '06' not in val and '60' not in val and '26' not in val and '46' not in val and '66' not in val and '86' not in val and '62' not in val and '64' not in val and '68' not in val:
        cnt += 1

print(cnt)

