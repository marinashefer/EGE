with open ('26_17537.txt') as file:
    n, m, k = map(int, file.readline().split())
    tickets = [list(map(int, i.split())) for i in file]

tickets = sorted(tickets, key=lambda x: (x[1], -x[0]))

hall = [m+1] * (k+1)
for r, m in tickets:
    hall[m] = r

ans = []
for i in range(1, k):
    r1, r2 = hall[i], hall[i+1]
    ans.append([min(r1, r2) - 1, i+1])

ans = sorted(ans, key = lambda x:(-x[0], -x[1]))

print(max(ans))