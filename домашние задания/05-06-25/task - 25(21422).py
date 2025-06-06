def f(num):
    ans = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            ans += [i, num//i]
    ans = sorted(set(ans))

    for i in ans:
        if str(i)[-1] == '7':
            if i != 7:
                return i
    return 0

cnt = 0
for i in range(1125000, 10**17):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break