with open("24_21717.txt") as f:
        data = f.read()

data = data.split("RSQ")

ans = 10**10
for i in range(len(data) - 130):
    s = "RSQ" + "RSQ".join(data[i:i + 129]) + "RSQ"
    end = data[i+129]
    cnt = 0
    for i in end:
        cnt += 1
        if i != 'Q':
            break
    if not end:
        cnt += 1
    ans = min(ans, (len(s) + cnt))

print(ans)



