from itertools import *

alph = sorted('ЦАПЛЯ')

ans = []
for pos, val in enumerate(product(alph, repeat = 5), start=1):
    val = ''.join(val)
    if val.count("А") <= 1:
        if val.count("Ц") == 2:
            if val.count("Л") == 0:
                ans.append(pos)

print(min(ans))