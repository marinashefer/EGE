with open ('26_1207 (1).txt') as file:
    s, n = map(int, file.readline().split())
    files = [int(i) for i in file]

files = sorted(files)

users = []
for file in files:
    if s >= file:
        s -= file
        users.append(file)
    else:
        break

s += users.pop()
files = sorted(files, reverse=True)

for file in files:
    if s >= file:
        users.append(file)
        break

print(len(users), users[-1])













