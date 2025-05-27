with open ('26_4684.txt') as file:
    n = file.readline()
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)

price1 = sum(prices) - (sum(prices[5::6]))//2
price2 = sum(prices) - (sum(prices[-len(prices)//6:]))//2
print(price1, price2)

#https://kompege.ru/variant?kim=25101705