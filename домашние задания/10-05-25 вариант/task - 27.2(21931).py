from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return max(distance)[1]

with open ('27_B_21931.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in file:
        x, y = (map(float, i.split()))
        if y > 17 and x < 17:
            cluster1.append((x, y))
        if y > 14 and x > 17:
            cluster2.append((x, y))
        if y < 17:
            cluster3.append((x, y))


center1 = centroid(cluster1)
center2 = centroid(cluster2)
center3 = centroid(cluster3)

print(len(cluster1), len(cluster2), len(cluster3))

print(int(10000*(center1[0])), int(10000*(center3[1])))