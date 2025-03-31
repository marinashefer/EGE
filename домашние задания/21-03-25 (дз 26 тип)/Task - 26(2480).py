with open ('26.txt') as file:
    n = int(file.readline())
    roads = [list(map(int, i.split())) for i in file]

roads = sorted(roads)

ans = []
for i in range(0, len(roads) - 1):
    if roads[i+1][0] <= roads[i][1]:
        ans.append(max(roads[i + 1][1], roads[i][1]) -  roads[i][0])
        roads[i] = [roads[i][0], max(roads[i+1][1], roads[i][1])]

print(len(ans), max(ans))