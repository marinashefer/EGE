from fnmatch import fnmatch

ans = []

for i in range(1234, 10**10, 1234):
    if fnmatch(str(i), '4*5*6'):
        if fnmatch(str(i), '?74*68?'):
            if i % 1234 == 0:
                print(i, i//1234)





