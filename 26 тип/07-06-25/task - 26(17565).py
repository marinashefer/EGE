with open ('26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    sailors = []
    for i in file:
        id0, ex1, ex2, ex3, ball = map(int, i.split())
        sailors.append([ex1+ex2+ex3, ball, id0])

sailors = sorted(sailors, key=lambda x: (-x[0], -x[1], x[2]))

if sailors[s-1][0] == sailors[s][0]:
    id_last = [sailor[2] for sailor in sailors if sailor[0] > sailors[s-1][0]][-1]
    cnt = len([1 for sailor in sailors if sailor[0] == sailors[s-1][0]])
else:
    id_last = sailors[s-1][2]
    cnt = 0

print(id_last, cnt)

#print(sailors[:s])
#print()
#print()
#print(sailors[s:s+10])