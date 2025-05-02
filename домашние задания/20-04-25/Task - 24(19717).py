with open ('24-19717.txt') as file:
    data = file.readline().strip()

l, r = 0, -1
cnt = 0
ans = -1

while True:
    if cnt <= 278:
        r += 1
        if r == len(data):
            break
        if data[r] == 'M':
            cnt += 1
    else:
        l += 1
        if data[l-1] == 'M':
            cnt -= 1

    if cnt <= 278:
        ans = max(ans, r-l+1)

print(ans)