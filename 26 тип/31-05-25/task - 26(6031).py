with open ('26_6031.txt') as file:
    n = int(file.readline())
    rings = [int(i) for i in file]

rings = sorted(rings, reverse=True)
last_ring = rings[0]
cnt = 1

for ring in rings:
    if last_ring - ring >= 6:
        cnt += 1
        last_ring = ring

print(cnt, last_ring)