with open ('26.2.txt') as file:
    n, v = map(int, file.readline().split())
    watermelons = [int(i) for i in file if 7000 <= int(i) <= 12000]

watermelons = sorted(watermelons, reverse=True)

ans_1 = 0
start_mass = 0
ans_2 = []
for watermelon in watermelons:
    if (watermelon + start_mass) <= (v * 1000):
        start_mass += watermelon
        ans_2.append(watermelon)
        ans_1 += 1

print(ans_1, min(ans_2))