with open ('26_2651.txt') as file:
    n = int(file.readline())
    ans = [[0]*9 for i in range(10000)]
    for i in range(n):
        year, type = map(int, file.readline().split())
        ans[year][type] += 1

cnt = 0
mx = 0
my = 0

for yea in range(1961, 1992):
    k = 0
    for typ in range(1, 9):
        if ans[yea][typ] == 0:
            k += 1
    cnt += k
    if cnt >= mx:
        mx = k
        my = yea

print(cnt, my)