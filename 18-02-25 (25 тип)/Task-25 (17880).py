from fnmatch import fnmatch

for i in range(1917, 10**10, 1917):
    if fnmatch(str(i),'3?12?14*5'):
        if i % 1917 == 0:
            print(i, i // 1917)