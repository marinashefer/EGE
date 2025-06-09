with open ('26_21719.txt') as file:
    n = int(file.readline())
    tasks = {}
    for i in file:
        ID, task = map(int, i.split())
        if ID not in tasks:
            tasks[ID] |= set()
        tasks[ID] |= {task}

tasks = sorted(tasks)

ans = []
cnt = 1
for i in range(len(tasks)-1):
    task1, task2 = tasks[i], tasks[i+1]
    if task2[0] == task
        if task2 - task1 == 0:
            continue
        if task2 - task1 == 1:
            cnt +=1