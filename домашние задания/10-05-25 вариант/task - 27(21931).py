from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return max(distance)[1]

with open ('27_A_21931.txt') as file:
    cluster1 = []
    cluster2 = []
    for i in file:
        x, y = (map(float, i.split()))
        if y > 14:
            cluster1.append((x, y))
        elif y < 14:
            cluster2.append((x, y))

center1 = centroid(cluster1)
center2 = centroid(cluster2)

print(len(cluster1), len(cluster2))

print(10000*int(center1[0]), 10000*int(center2[1]))