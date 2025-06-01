with open ('26_6641.txt') as file:
    n, m = map(int, file.readline().split())
    products = []
    for i in file:
        num, let = i.split()
        products.append([int(num), let])

products = sorted(products)

products_S = []
products_W = []
for p in products.copy():
    if p[0] <= m:
        m -= p[0]
        if p[1] == 'S': products_S.append(p[0])
        else: products_W.append(p[0])
        products.remove(p)

for p in products:
    if p[1] == 'S' and m + products_W[-1] - p[0] >= 0:
        m += products_W[-1] - p[0]
        products_S.append(p[0])
        products_W.pop()

print(len(products_S), m)