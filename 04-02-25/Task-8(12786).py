from itertools import permutations

cnt = 0
for val in set(permutations('МАКАКА', 6)):
    val = ''.join(val)
    if ('АА' not in val) and ('КК' not in val):
        cnt += 1

print(cnt)