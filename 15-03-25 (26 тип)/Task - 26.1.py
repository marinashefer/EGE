with open ('26-1.txt') as file:
    n, m , k = map(int, file.readline().split())
    ships = [list(map(int, i.split())) for i in file]

ships = sorted(ships, key = lambda x: (x[1], -x[0]))

pole = [m+1] * (k+1)
for hor, ver in ships:
    pole[ver] = hor

ans = []
for i in range(1, len(pole) - 1):
    p1, p2 = pole[i], pole[i+1]
    ans.append([min(p1, p2) - 1, i])

ans = sorted(ans, key = lambda x: (-x[0], x[1]))

print(max(ans))