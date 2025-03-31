print('x y w z')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                f = ((not (w <= (x == (y or y)))) and (z <= x))
                if f:
                    print(x, y, w, z, f)