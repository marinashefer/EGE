from itertools import *

def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 1000):
    num3 = convert(n, 3)
    if n % 5 == 0:
        num3 = num3 + num3[-3:]
    else:
        num3 = num3 + convert((n % 5) * 5, 3)

    if int(num3, 3) < 5496:
        ans.append([n, int(num3, 3)])

print(max(ans))