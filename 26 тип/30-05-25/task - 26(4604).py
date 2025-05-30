with open ('26_4604 (2).txt') as file:
    n = file.readline()
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
last_box = boxes[0]
cnt = 1
for box in boxes:
    if last_box - box >= 3:
        last_box = box
        cnt += 1

print(cnt, last_box)
