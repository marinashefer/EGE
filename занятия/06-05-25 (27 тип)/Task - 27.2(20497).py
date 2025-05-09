from math import dist

with open ('27.19.B_20497.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 3
clusters = []

while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)

def centroid(cluster):
    distance =[]
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return max(distance)[1]

ends = [centroid(cluster) for cluster in clusters]

ans_x = sum([end[0] for end in ends])/len(ends)
ans_y = sum([end[1] for end in ends])/len(ends)

print(int(ans_x * 10000), int(ans_y * 10000))