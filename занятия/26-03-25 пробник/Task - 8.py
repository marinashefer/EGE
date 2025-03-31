from itertools import product

alph = sorted('ЛУНАТИК')
ans = []
for pos, val in enumerate(product(alph, repeat=6), 1):
    val = ''.join(val)
    val = val.replace('У', '*').replace('А', '*').replace('И', '*')
    if val[0] == 'Н' and val.count('*') == 1:
        ans.append([pos, val])

print(max(ans))