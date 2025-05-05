from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open ('27A_19747.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
eps = 0.6

while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

#print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]

ans_x = sum(center[0] for center in centers) / len(centers)
ans_y = sum(center[1] for center in centers) / len(centers)

print(int(ans_x*100000), int(ans_y*100000))