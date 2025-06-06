from itertools import product

ans = []
for r in range(0, 3):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for q1 in '0123456789':
            for q2 in '0123456789':
                num = int('1' + z + '2' + q1 + q2 + '76')
                if num % 1923 == 0:
                    if num < 10**8:
                        ans.append([num, num // 1923])

ans = sorted(ans)
for i in ans:
    print(*i)