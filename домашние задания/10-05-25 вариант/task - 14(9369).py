from string import digits, ascii_lowercase
ans = []
alph = digits + ascii_lowercase
for x in alph[:16]:
    for y in alph[:16]:
        num = int('27a' + x + '23', 16) + int('8' + y + 'e5d2', 16)
        if num % 5 == 0:
            ans.append(int(x, 16) + int(y, 16))
print(max(ans))