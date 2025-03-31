from itertools import product

ans = []
for r in range(1, 4):
    for b in product('13579', repeat=r):
        b = ''.join(b)
        for a in '02468':
            num = int('1' + a + '2157' + b + '4')
            if num % 133 == 0 and num <= 10**10:
                ans.append([num,num // 133])

ans = sorted(ans)
for i in ans:
    print(*i)