from itertools import product

ans = []
for r in range(0, 4):
    for z in product('0123456789', repeat = r):
        for q in '0123456789':
            z = ''.join(z)

            num = int('1' + q + '2139' + z + '4')
            if num % 3052 == 0:
                ans.append([num, num // 3052])

ans = sorted(ans)
for i in ans:
    print(*i)