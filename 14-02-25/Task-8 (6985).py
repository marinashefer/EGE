from itertools import product

alph = sorted('МАРКСЛ')

ans_2 = []
for pos, val in enumerate(product(alph, repeat=6), 1):
    val = ''.join(val)
    if 'СК' not in val and 'КС' not in val:
        ans = [val.count('М'), val.count('А'), val.count('Р'), val.count('К'), val.count('С'), val.count('Л')]
        if ans.count(3) == 1 and ans.count(1) == 3:
            ans_2.append([pos, val])

print(max(ans_2))