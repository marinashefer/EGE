from string import ascii_uppercase

with open ('24_9791.txt') as file:
    data = file.readline()

for c in ascii_uppercase[6:]:
    data = data.replace(c, ' ')

data = data.split()

ans = 0
for i in data:
    #убираем ведущие нули
    s = i.lstrip('0')
    if int(s, 16) % 20 == 0:
        ans = max(ans, len(s))
    else:
        #перебираем все последовательности
        for l in range(len(s)):
            for r in range(len(s), l, -1):
                ps = s[l:r]
                if int(ps, 16) % 20 == 0:
                    ans = max(ans, len(ps))
                    break

print(ans)