with open ('26_7602.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times)
cels = [0] * k
last_cell = 0
cnt = 0

for time in times:
    for i in range(k):
        if time[0] >= cels[i]:
            cels[i] = time[1] + 1
            cnt += 1
            last_cell = i + 1
            break

print(cnt, last_cell)

