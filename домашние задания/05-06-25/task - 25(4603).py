from itertools import product

ans = []
for r in range(0, 4):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        num = int('1234' + z + '7')
        if num % 141 == 0:
            if num < 10**8:
                ans.append([num, num//141])

ans = sorted(ans)
for i in ans:
    print(*i)