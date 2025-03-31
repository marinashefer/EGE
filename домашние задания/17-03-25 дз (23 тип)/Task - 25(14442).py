from fnmatch import fnmatch

ans = []
for i in range(400000, 500001):
    if fnmatch(str(i), '*7?'):
        ans.append(i)

if len(ans) >= 18:
    print(i, sum(ans))