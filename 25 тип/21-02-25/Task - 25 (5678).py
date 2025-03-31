from itertools import product

ans = []
for r1 in range(0, 3):
    for r2 in range(0, 3):
        if r1 + r2 <= 2:
            for z1 in product('0123456789', repeat=r1):
                z1 = ''.join(z1)
                for z2 in product('0123456789', repeat=r2):
                    z2 = ''.join(z2)
                    num = int('124'+ z1 + '5' + z2 + '79')
                    summ = sum([int(i) for i in str(num) if int(i) % 2 != 0])
                    if num <= 10**8 and num % summ == 0:
                        ans.append([num, sum([int(i) for i in str(num)])])

ans = sorted(ans)
for i in ans:
    print(*i)



