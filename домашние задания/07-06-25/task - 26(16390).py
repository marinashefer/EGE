with open ( '26_16390.txt') as file:
    s, n = map(int, file.readline().split())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)

ans = []
for box in boxes:
    if box <= s:
        ans.append(box)
        s -= box
    else:
        break

s += ans.pop()

boxes = sorted(boxes, reverse=True)
for box in boxes:
    if box <= s:
        ans.append(box)
        break

print(len(ans), ans[-1])
