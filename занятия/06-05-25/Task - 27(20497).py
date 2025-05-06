from math import dist
import turtle

turtle.tracer(0)

with open ('27.19.A_20497.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.4
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

print([len(cluster) for cluster in clusters])

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return max(distance)[1]

#понт-черепаха
turtle.up()
colors= ['black', 'pink', 'blue']
for cluster, color in zip(clusters, colors):
    for dot in cluster:
        turtle.goto(dot[0] * 100, dot[1]*150)
        turtle.dot(3, color)

turtle.update()
turtle.done()

ends = [centroid(cluster) for cluster in clusters]

ans_x = sum(end[0] for end in ends) / len(ends)
ans_y = sum(end[1] for end in ends) / len(ends)

print(int(ans_x * 10000), int(ans_y * 10000))