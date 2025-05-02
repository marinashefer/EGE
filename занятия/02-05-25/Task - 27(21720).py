from math import dist

clusters = []
eps = 2

with open ('27_A_21720 (1).txt') as file:
    data = [list(map(float, i.split())) for i in file]

while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

# print([len(cluster) for cluster in clusters]) (!)

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

center1 = centroid(clusters[0])
center2 = centroid(clusters[1])

ans_x = (center1[0] + center2[0]) / 2
ans_y = (center1[1] + center2[1]) / 2

print(int(ans_x * 10000), int(ans_y * 10000))