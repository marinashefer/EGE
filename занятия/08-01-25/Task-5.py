ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r.replace('1', '11')
    else:
        r = r.replace('0', '00')
    if int(r, 2) > 70:
        ans.append(n)

print(min(ans))