from fnmatch import fnmatch

for i in range(2024, 10**10, 2024):
    if fnmatch(str(i), '1?2157*4'):
        if i % 2024 == 0:
            print(i, i // 2024)