with open ('26_12256.txt') as file:
    s, n = map(int, file.readline().split())
    moms = [int(i) for i in file]

moms = sorted(moms)

boxes = []
for mom in moms:
    if s >= mom:
        s -= mom
        boxes.append(mom)
    else:
        break

s += boxes.pop()

moms = sorted(moms, reverse=True)
for mom in moms:
    if s >= mom:
        boxes.append(mom)
        break

print(len(boxes), boxes[-1])
