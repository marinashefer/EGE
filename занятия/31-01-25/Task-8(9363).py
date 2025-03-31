from itertools import permutations

cnt = 0
for val in set(permutations('ХОЧУНАБЮДЖЕТ', 12)):
    val = ''.join(val)
    for i in permutations('УАЮЕО', 5):
        i = ''.join(i)
        if i not in val:
            cnt += 1

print(cnt)