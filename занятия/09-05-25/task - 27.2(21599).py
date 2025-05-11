from math import dist
import turtle

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]


with open('27_B_21599.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    cluster5 = []
    cluster6 = []
    for i in file:
        x, y = map(float, i.split())
        if x < - 13 and y < (-2 * x - 25):
            cluster1.append((x, y))
        if x < -9 and y > (-2 * x - 25):
            cluster2.append((x, y))
        if x > -9 and (y > 1.5714285714 * x + 11):
            cluster3.append((x, y))
        if (y < 1.5714285714 * x + 11) and y > x + 1:
            cluster4.append((x, y))
        if (y > -5) and y < x + 1:
            cluster5.append((x, y))
        if y < -5:
            cluster6.append((x, y))

center1 = centroid(cluster1)
center2 = centroid(cluster2)
center3 = centroid(cluster3)
center4 = centroid(cluster4)
center5 = centroid(cluster5)
center6 = centroid(cluster6)

ans_x = (center1[0] + center2[0] + center3[0] + center4[0] + center5[0] + center6[0]) / 6
ans_y = (center1[1] + center2[1] + center3[1] + center4[1] + center5[1] + center6[1]) / 6

print(int(ans_x * 10000), int(ans_y * 10000))



















