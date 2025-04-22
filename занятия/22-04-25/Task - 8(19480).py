from itertools import permutations

alph = 'ПАРИЖАНКА'
cnt = 0

for val in set(permutations(alph)):
    val = ''.join(val)
    val = val.replace('И', 'А')
    if val.count('АА')  == 1:
        if 'ААА' not in val:
            cnt += 1

print(cnt)