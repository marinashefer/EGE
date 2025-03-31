print('x y w z')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                f = ((z <= (not (y <= x))) or w)
                if f == 0:
                    print(x, y, w, z, f)

