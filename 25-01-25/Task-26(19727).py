with open ('26.1.txt') as file:
    m, n = map(int, file.readline().split())
    containers = [int(i) for i in file]

containers = sorted(containers)

ans_1 = 0
mass = 0
for container in containers:
    if container + mass <= m:
        mass += container
        ans_1 += 1

ans_2 = 0
for container in containers[::-1]:
    if sum(containers[:ans_1 - 1]) + container > m:
        ans_2 += 1

print(ans_1, ans_2)