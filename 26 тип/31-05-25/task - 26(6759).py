with open ('26_6759.txt') as file:
    n = int(file.readline())
    products = [int(i) for i in file]

products = sorted(products, reverse=True)

price1 = sum(products) - sum(products[:n//3])

price2 = sum(products) - sum(products[2::3])
print(price1, price2)