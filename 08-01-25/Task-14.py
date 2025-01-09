ans = []
for x in range(1, 5770):
    num = 9**2025 + 9*1000 - x
    count = 0
    while num:
        if num % 9 == 0:
            count += 1
        num //= 9
        if count == 1026:
            ans.append(int(x))

print(max(ans))