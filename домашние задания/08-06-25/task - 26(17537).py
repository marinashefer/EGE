with open ('26_17537 (1).txt') as file:
    n, m, k = map(int, file.readline().split())
    places = [m] * (k+1)
    for i in file:
        row, col = map(int, i.split())
        places[col] = min(places[col], row-1)

ans = []
for i in range(2, k-1):
    place1, place2 = places[i], places[i+1]
    ans.append([min(place1, place2), i])

print(max(ans))