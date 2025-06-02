ans = []
for n in range(1, 1000):
    r = bin(n)[2:]
    r = r + str(sum(map(int, r)) % 2)
    r = r + str(sum(map(int, r)) % 2)

    if int(r, 2) > 75:
        ans.append(int(r, 2))

print(min(ans))