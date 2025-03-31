from fnmatch import fnmatch

for i in range(141, 10**8, 141): #for i in range(1234 - 1234 % 141, 10**8, 141):
    if fnmatch(str(i), '1234*7'):
        if i % 141 == 0:
            print(i, i // 141)