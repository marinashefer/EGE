from itertools import product

def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    return res

ans = []
for r in range(3):
    for q in product('0123456789', repeat=r):
        q = ''.join(q)
        for z in '0123456789':
            num = int(f'12{q}{z}45')
            if len(list(f(num))) == 18:
                ans.append([num, max(f(num))])

print(*ans)















