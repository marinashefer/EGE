ans = []

for q1 in '012345678':
    for q2 in '012345678':
        num = int('1234' + q1 + '57' + q2 + '8')
        if num % 17 == 0 and num <= 10**9:
            ans.append([num, num //17])

ans = sorted(ans)
for i in ans:
    print(*i)