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
for i in range(700001, 10**15):
    func = f(i)
    if func:
        cnt += 1
        print(i, func)
        if cnt == 5:
            break
