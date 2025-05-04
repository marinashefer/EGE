from fnmatch import fnmatch

def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            if fnmatch(str(i), '4*'):
                res |= {i}
            elif fnmatch(str(num//i), '4*'):
                res |= {num//i}
    return res

for i in range(1, 10**6):
    if len(f(i)) == 24:
        print(i, max(f(i)))