from string import digits
from itertools import product

alph = digits

cnt = 0
for val in product(alph[:9], repeat=7):
    val = ''.join(val)
    if val[0] not in '0246' and val[-3:] != '000' and val[-3:] != '111' and val[-3:] != '222' and val[-3:] != '333'\
            and val[-3:] != '444' and val[-3:] != '555' and val[-3:] != '666' and\
            val[-3:] != '777' and val[-3:] != '888' and val[-3:] != '999':
        cnt += 1

print(cnt)