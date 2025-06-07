with open ('26_17643 (1).txt') as file:
    n = int(file.readline())
    products = {}
    average = []
    for i in file:
        art, price, stat = map(int, i.split())
        average.append(price)
        if art not in products:
            products[art] = [0, price, 0] # кол-во проданных, цена, кол-во остатков
        if stat: #если товар не продан
            products[art][2] += 1
        else:
            products[art][0] += 1

average = sum(average) / len(average)
products = [i for i in products.values() if i[1] > average]

products = sorted(products, key=lambda x: (-x[0], -x[1], x[2]))
leader = products[0]

print(leader[0] * leader[1], leader[2])