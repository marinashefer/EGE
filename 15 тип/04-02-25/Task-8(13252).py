from itertools import permutations, product



count = 0
for val in set(permutations('КИДАЛА', 5)):
    val = ''.join(val)
    if 'АА' not in val:
        count += 1

print(count)
