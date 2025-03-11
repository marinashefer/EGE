from itertools import permutations

cnt = 0

for val in set(permutations('СОВЕСТЬ')):
    val = ''.join(val)
    val = val.replace('О', '*')
    val = val.replace('Е', '*')
    val = val.replace('Ь', '*')
    val = val.replace('С', '-')
    val = val.replace('В', '-')
    val = val.replace('Т', '-')
    if '**' not in val:
        if '--' not in val:
            cnt += 1

print(cnt)