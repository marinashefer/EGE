from itertools import product
from string import digits

alph = digits

cnt = 0
for val in product(alph[:6], repeat=6):
    val = ''.join(val)
    if val.count('0') == 1 and '10' not in val and '01' not in val and '30' not in val and '03' not in val and '50' not in val and '05' not in val:
        cnt += 1

print(cnt)