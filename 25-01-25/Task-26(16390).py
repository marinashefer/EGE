with open ('26.3.txt') as  file:
    s, n = map(int, file.readline().split())
    packages = [int(i) for i in file]

packages = sorted(packages)

ans_1 = 0
mass = 0
last_package = 0
for package in packages:
    if mass + package <= s:
        mass += package
        ans_1 += 1
        last_package = package

mass -= last_package
for package in packages[::-1]:
    if mass + package <= s:
        last_package = package
        break

print(ans_1, last_package)