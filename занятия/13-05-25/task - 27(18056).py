from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open ('27A_18056.txt') as file:
    cluster1 = []
    cluster2 = []
    for i in file:
        x, y = (map(float, i.split()))
        if y > -1 and x < 1:
            cluster1.append((x, y))
        if y < -1 and x > 0:
            cluster2.append((x, y))


center1 = centroid(cluster1)
center2 = centroid(cluster2)

ans_x = (center1[0] + center2[0]) / 2
ans_y = (center1[1] + center2[1]) / 2

print(int(ans_x*100000), int(ans_y*100000))