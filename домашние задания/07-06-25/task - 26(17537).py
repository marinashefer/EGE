with open ('26_17537.txt') as file:
    n, m, k = map(int, file.readline().split())
    tickets = [m] * (k+1)
    for i in file:
        row, col = map(int, i.split())
        tickets[col] = min(tickets[col], row-1)

ans = []
for i in range(2, k+1):
    place1, place2 = tickets[i-1], tickets[i]
    ans.append([min(place1, place2), i])

print(max(ans))