from fnmatch import fnmatch

ans = []
for num in range(2023, 10**9+1, 2023):
    if fnmatch(str(num), '20*23'):
        if num % 2023 == 0:
            if sum(map(int, str(num))) % 7 == 0 and sum(map(int, str(num))) < 20:
                ans.append(num)

ans = sorted(ans)
print(ans)