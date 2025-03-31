from itertools import product

ans = []
for r in range(0, 3):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for q1 in '0123456789':
            for q2 in '0123456789':
                for q3 in '0123456789':
                    num = int('12' + q1 + '3' + z + '456' + q2 + q3 + '9')
                    if num %  98591 == 0 and num <= 10**12:
                        ans.append([num, num//98591])

ans = sorted(ans)
print(ans)