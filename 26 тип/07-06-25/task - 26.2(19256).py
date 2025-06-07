with open ('26_19256.txt') as file:
    n = int(file.readline())
    students = {}
    for i in file:
        id0, num = map(int, i.split())
        if id0 not in students:
            students[id0] = set()
        students[id0] |= {num}

ans = []
for id0 in students:
    student = sorted(students[id0])
    cnt = 1
    max_cnt = 0
    for i in range(len(students) - 1):
        task1, task2 = students[i], students[i + 1]
        if task2 - task1 == 1:
                cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    ans.append([max_cnt, student])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))
print(ans[0])