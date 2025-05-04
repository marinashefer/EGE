ans = []
for i in range(1, 100):
    ans.append(2**i)

def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 and i in ans:
            res |= {i}
        elif num % (num//i) == 0 and (num//i in ans):
            res |= {num//i}
    return len(res)

def f2(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 and i not in ans:
            res |= {i}
        elif num//i not in ans:
            res |= {num//i}
    return sum(res)

cnt = 0
for n in range(10**6+1, 10**10):
    if f(n) >= 20:
        print(n, f2(n))
        cnt += 1
        if cnt == 5:
            break
