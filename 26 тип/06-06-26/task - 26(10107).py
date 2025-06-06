with open ('26_10107 (1).txt') as file:
    n = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: x[1])

approved = [events[0]]
for event in events:
    if approved[-1][1] <= event[0]:
        approved.append(event)

ans = approved[-1][0] - approved[-2][1]
print(len(approved), ans)