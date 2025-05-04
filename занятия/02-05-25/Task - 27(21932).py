from math import dist

with open ('27_A_21932.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 1
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

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]

ans_x = min([center for center in centers], key = lambda x: x[1])[2][0]
ans_y = max([center for center in centers], key = lambda x: x[1])[2][1]

print(int(ans_x * 10000), int(ans_y * 10000))