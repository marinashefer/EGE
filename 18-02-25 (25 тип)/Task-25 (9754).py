from itertools import product

ans = []
for r  in range(0, 4):
    for z in product('0123456789', repeat=r):
        for q in '0123456789':
            z = ''.join(z)
            num = int('3' + q + '1' + z + '57')
            if num % 2023 == 0:
                ans.append([num, num // 2023])


ans = sorted(ans)
for i in ans:
    print(*i)