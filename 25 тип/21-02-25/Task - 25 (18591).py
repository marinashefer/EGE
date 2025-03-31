ans = []
for q1 in '0123456789':
    for c1 in '2468':
        for c2 in '02468':
            for n in '13579':
                for q2 in '0123456789':
                    num = int(c1 + '9' + q1 + '23' + q2 + '23' + n + c2)
                    if num % 1984 == 0 and num <= 10**10:
                        ans.append([num, num // 1984])

ans = sorted(ans)
for i in ans:
    print(*i)