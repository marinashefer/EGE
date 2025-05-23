from math import dist

with open ('27_A_21911.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 2
clusters = []

while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

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

#centers = [centroid(cluster) for cluster in clusters]
ans_x = sum(centroid(cluster)[0] for cluster in clusters) / len(clusters)
ans_y = (center1[1] + center2[1]) / 2

print(int(ans_x*10000), int(ans_y*10000))