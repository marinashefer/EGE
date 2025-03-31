from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase

for val in product(alph[:12], repeat=7):
    val = ''.join(val)
    if val.count('B') == 2:
        if 