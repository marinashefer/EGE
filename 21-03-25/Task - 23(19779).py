def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            if is_prime(i) and str(i)[-3:] == '777':
                res |= {i}
            if is_prime(num//i) and str(num//i)[-3:] == '777':
                res |= {num//i}

