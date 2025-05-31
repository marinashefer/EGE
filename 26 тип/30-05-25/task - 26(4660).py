with open ('26_4660 (3).txt') as file:
    n = file.readline()
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)

customer = sum(prices) - sum(prices[3::4]) // 2
shop = sum(prices) - sum(prices[-len(prices)//4:]) // 2

print(customer, shop)