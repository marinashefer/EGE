with open ('26_8512.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    passengers = [list(map(int, i.split())) for i in file]

passengers = sorted(passengers)
cnt = 0
cells = [0] * k
last_cell = 0
for passenger in passengers:
    for i in range(k):
        if passenger[0] >= cells[i]:
            cells[i] = passenger[1] + 1
            cnt += 1
            last_cell = i + 1
            break

print(cnt, last_cell)
