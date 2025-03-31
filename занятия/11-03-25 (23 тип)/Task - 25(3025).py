def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        res |= {i, num //i}
    sorted(res)

#https://kompege.ru/variant?kim=25087374