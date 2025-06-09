with open ('26_9793.txt') as file:
    n = int(file.readline())
    details = []
    for pos, val in enumerate(file, start=1):
        sh, po = map(int, val.split())
        details.append([sh, 1, pos])
        details.append([po, 0, pos])

details = sorted(details)

conveyor = [0] * n
last = 0
for time, type, num in details:
    if num not in conveyor:
        if type == 1:
            vacant = conveyor.index(0)
            conveyor[vacant] = num
        else:
            vacant = conveyor[::-1].index(0)
            conveyor[n - vacant - 1] = num
        last = num

print(last, conveyor.index(last))

