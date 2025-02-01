with open ('26.1.txt') as file:
    n = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1], -x[0]))

true_events = [events[0]]

for event in events:
    if event[0] >= true_events[-1][1]:
        true_events.append(event)

print(len(true_events), true_events[-2:], events[-10:])