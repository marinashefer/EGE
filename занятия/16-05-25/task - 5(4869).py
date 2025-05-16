for n in range(2, 1000):
    ans = []
    r = bin(n)[2:]
    for i in r:
        ans.append(i)
    cnt_1 = 0
    cnt_0 = 0
    for i in ans:
        if ans.index(i) % 2 != 0:
            if i == '1':
                cnt_1 += 1
        if ans.index(i) % 2 == 0:
            if i == '0':
                cnt_0 += 1

    if abs(cnt_1 - cnt_0) == 5:
        print(n)
        break
