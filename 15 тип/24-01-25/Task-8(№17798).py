from itertools import product

alph = sorted('МИНУС')

ans = []
for num, val in enumerate(product(alph, repeat = 4), 1):
    val = ''.join(val)
    if val.count('И') + val.count('У') <= val.count('М') + val.count('Н') + val.count('С'):
        ans.append(num)

print(ans[-1])

