def delit(num):
    ans = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            ans += [i, num//i]
    ans = sorted(set(ans))

    for i in ans:
        if str(i)[-1] == '9':
            if i != 9:
                return i
    return 0

cnt = 0
for i in range(800001, 10**10):
    func = delit(i)
    if func:
        cnt += 1
        print(i, func)
        if cnt == 5:
            break