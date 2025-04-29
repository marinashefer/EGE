from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open ('27_A_17882.txt') as file:
    cluster_1 = []
    cluster_2 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 1:
            cluster_1.append((x, y))
        else:
            cluster_2.append((x, y))

center1 = centroid(cluster_1)
center2 = centroid(cluster_2)

ans_x = (center1[0] + center2[0]) / 2
ans_y = (center1[1] + center2[1]) / 2

print(int(ans_x * 10000), int(ans_y * 10000))