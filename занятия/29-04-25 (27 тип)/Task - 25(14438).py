from fnmatch import fnmatch
from itertools import *

for r in range(6):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v1 in '0123456789':
            for v2 in '0123456789':
                num = int('17' + z + '46' + v1 + v2 + '8')
                if num <= 10**12:
                    if num % 86513 == 0:
                        summ = sum(map(int, str(num)))
                        if summ**0.5 == int(summ**0.5):
                            print(num, num //86513)