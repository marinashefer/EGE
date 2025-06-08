with open ('26.txt') as file:
    n = int(file.readline())
    dots = [list(map(int, i.split())) for i in file]

dots = sorted(dots ,key= lambda x:(x[0], x[1]))

print(dots[15000:15010])
ans = []
cnt = 0
for dot1, dot2 in zip(dots, dots[1:]):
    if dot1[0] == dot2[0]:
        if dot2[1] - dot1[1] - 1 == 1:
            cnt += 1
            ans.append([cnt*2, dot2[0]])
    else:
        cnt = 0

print(ans)
print(max(ans))