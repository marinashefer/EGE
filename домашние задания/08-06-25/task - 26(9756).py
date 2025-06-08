with open ('26_9756.txt') as file:
    n = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1]))

approved = [events[0]]

for event in events:
    if approved[-1][1] <= event[0]:
        approved.append(event)

last = approved.pop()

events = sorted(events, key=lambda x: (-x[1]))
for event in events:
    if approved[-1][1] <= event[0]:
        approved.append(event)
        break

print(len(approved)+1, approved[-1][1])