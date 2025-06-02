with open ('26_21424.txt') as file:
    n = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

last_box = boxes[0]
cnt = 1

for box in boxes:
    if last_box - box >= 9:
        cnt += 1
        last_box = box

print(cnt, last_box)

