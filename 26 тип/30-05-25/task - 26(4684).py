with open ('26_4684 (2).txt') as file:
    n = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)
customer = sum(prices) - sum(prices[5::6]) // 2

prices = sorted(prices)
shop = sum(prices) - sum(prices[:n//6]) // 2

print(customer, shop)