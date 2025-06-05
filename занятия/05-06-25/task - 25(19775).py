def is_prime(num):
    if num < 2: return 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def deliteli(num):
    ans = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            ans += [i, num//i]
    ans = set(ans)

    ans_prime = []
    for i in ans:
        if is_prime(i):
            ans_prime.append(i)

    if len(ans_prime) < 2:
        s = 0
    else:
        s = sum(ans_prime)

    if s != 0 and s % 145 == 0:
        return s
    else:
        return 0

cnt = 0
for i in range(32500000,10**30):
    if deliteli(i):
        print(i, deliteli(i))
        cnt += 1
        if cnt == 7:
            break

















