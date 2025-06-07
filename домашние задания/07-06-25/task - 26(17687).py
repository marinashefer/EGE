with open ( '26_17687.txt') as file:
    n = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)

price1 = sum(prices) - sum(prices[:n//9])
price2 = sum(prices) - sum(prices[8::9])
print(price1, price2)