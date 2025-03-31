from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase

nechet = '13579BDFHJLN'
chislo = '012345'

count = 0
for val in product(alph[:25], repeat=4):
    val = ''.join(val)
    if ((val[0] in nechet) + (val[1] in nechet) + (val[2] in nechet) + (val[3] in nechet)) == 1:
        if ((val[0] in '12345') + (val[1] in chislo) + (val[2] in chislo) + (val[3] in chislo)) <= 2:
            if val[0] != '0':
                count += 1

print(count)
