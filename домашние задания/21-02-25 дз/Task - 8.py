from itertools import *

alph = sorted('КАЛЕЙДОСКОП')

ans = []

for pos, val in enumerate(product(alph, repeat=6), 0):
    val = ''.join(val)
    if pos % 2 == 0:
        if val[0] != '0':
            if val[0] == 'К':
                if val.count('С') == 0 and val.count('Е') == 0:
                    if val.count('Й') >= 2:
                        ans.append(pos)

print(min(ans))











