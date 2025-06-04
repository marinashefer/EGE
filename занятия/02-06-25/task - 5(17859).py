ans = []
for n in range(1, 13):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'

    ans.append(int(r, 2))

print(max(ans))