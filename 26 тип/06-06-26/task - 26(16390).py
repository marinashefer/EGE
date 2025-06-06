with open ('26_16390 (1).txt') as file:
    s, n = map(int, file.readline().split())
    kids = [int(i) for i in file]

kids = sorted(kids)

cnt = []
for kid in kids:
    if s >= kid:
        s -= kid
        cnt.append(kid)
    else:
        break

s += cnt.pop()

kids = sorted(kids, reverse=True)
for kid in kids:
    if s >= kid:
        cnt.append(kid)
        break

print(len(cnt), cnt[-1])