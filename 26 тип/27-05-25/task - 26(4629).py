with open ('26_4629.txt') as file:
    n = file.readline()
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)
price1 = sum(prices) - (sum(prices[:len(prices)//4])//2)
price2 = sum(prices) - (sum(prices[-len(prices)//4:])//2)
print(price1, price2)