print('a b c')

for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            f = (a and (not b)) or c
            print(a, b, c, f)