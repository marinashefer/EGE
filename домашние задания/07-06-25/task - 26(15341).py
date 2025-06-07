with open ('26_15341.txt') as file:
    n = int(file.readline())
    cakes = [int(i) for i in file]

cakes = sorted(cakes, reverse=True)

cnt = 1
last_cake = cakes[0]
for cake in cakes:
    if last_cake - cake >= 8:
        cnt += 1
        last_cake = cake

print(cnt, last_cake)