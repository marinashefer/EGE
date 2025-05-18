def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(1, 10001)[::-1]:
    num= 6**900 + 6**10 - x
    num6 = convert(num,  6)
    if num6.count('3') == num6.count('5'):
        print(x)
        break