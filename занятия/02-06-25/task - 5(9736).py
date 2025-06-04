ans = []

for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin(((n % 3) * 3))[2:]

    if int(r, 2) <= 170:
        ans.append(int(r, 2))

print(max(ans))