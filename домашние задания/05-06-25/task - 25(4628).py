from itertools import product

ans = []
for r in range(0, 3):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for q in '0123456789':
            num = int('12' + z + '4' + q + '65')
            if num % 161 == 0:
                if num < 10**8:
                    ans.append([num, num//161])

ans = sorted(ans)
for i in ans:
    print(*i)