from itertools import product
from string import digits, ascii_lowercase

alph = digits + ascii_lowercase
for val in product(alph[:15], repeat=5):
    val = ''.join(val)
    if val.count('8') == 1 and