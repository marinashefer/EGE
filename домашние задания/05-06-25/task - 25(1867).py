def delit(num):
    ans = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            ans += [i, num//i]
    ans = sorted(set(ans))

    for i in ans:
        if str(i)[-1] == '8':
            if i != 8:
                return i
    return 0

cnt = 0
for i in range(500001, 10**10):
    if delit(i):
        cnt += 1
        print(i, delit(i))
        if cnt == 5 :
            break
