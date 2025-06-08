with open ('26_10107 (1).txt') as file:
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times, key=lambda x: (x[1]))

ans = [times[0]]
for time in times:
    if ans[-1][1] <= time[0]:
        ans.append(time)

last = ans.pop()

print(len(ans)+1, max(times)[0] - ans[-1][1])