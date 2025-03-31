def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

cnt = 0
for num in range(600001, 10**20):
    if num % 6 == 0:
        if is_prime(num-1):
            if is_prime(num+1):
                cnt += 1
                print(num-1, num+1)
                if cnt == 6:
                    break

