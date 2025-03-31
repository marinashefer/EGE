print('x y w z u')

for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                for u in range(0, 2):
                    f = ((z <= w) and (y == (not x))) <= (u ==(y or z))
                    if f == 0:
                        print(x, y, w, z, u, f)