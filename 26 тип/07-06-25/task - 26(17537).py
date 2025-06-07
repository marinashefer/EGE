with open ('26_17537 (2).txt') as file:
    n, m, k = map(int, file.readline().split())
    tickets = [m] * (k+1)
    for i in file:
        row, col = map(int, i.split())
        tickets[col] = min(tickets[col], row-1)

ans = []
for i in range(2, k+1):
    ticket1, ticket2 = tickets[i], tickets[i-1]
    ans.append([min(ticket1, ticket2), i])

print(max(ans))