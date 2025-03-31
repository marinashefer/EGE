from fnmatch import fnmatch

for i in range(7777, 10**10, 7777):
    if fnmatch(str(i), '12*567?'):
        if i % 7777 == 0:
            print(i, i // 7777)