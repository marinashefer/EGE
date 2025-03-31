from string import digits, ascii_uppercase
from itertools import product

alph = digits +ascii_uppercase


for val in product(alph[:20], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if ((int(val[0]) + int(val[1])) % 2) == 1 and ((int(val[1]) + val[2]) % 2) == 1 and ((val[2] + val[3]) % 2) == 1 \
                and ((val[3] + val[4]) % 2) == 1:
