ans = []

for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '01'
    else:
        r = '1' + r + '1'
    if int(r, 2) > 156:
        ans.append(n)

print(min(ans))