from fnmatch import fnmatch

for i in range(98591, 10**12, 98591):
    if fnmatch(str(i), '12?3*456??9'):
        if i % 98591 == 0:
            print(i, i // 98591)