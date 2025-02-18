from itertools import product

ans = []
for r in range(0, 3):
    for z in product('0123456789', repeat=r):
        for q in '0123456789':
            z = ''.join(z)
            num = int('12' + z + '34' +  q + '5')
            if num % 2025 == 0:
                ans.append([num, num//2025])

ans = sorted(ans)
for i in ans:
    print(*i)




