from itertools import permutations

cnt = 0
for val in set(permutations('СОТОЧКА', 7)):
    val = ''.join(val)
    val = val.replace('О', '*')
    val = val.replace('А', '*')
    if '**' in val:
        cnt += 1

print(cnt)