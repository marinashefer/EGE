with open ('26_17881.txt') as file:
    n = int(file.readline())
    students = []
    for i in file:
        ID, ex1, ex2, ex3, ex4 = map(int, i.split())
        if ex1 != 2 and ex2 != 2 and ex3 != 2 and ex4 != 2:
            students.append([ex1+ex2+ex3+ex4, ID, 0])
        else:
            cnt = [ex1, ex2, ex3, ex4]
            students.append([ex1 + ex2 + ex3 + ex4, ID, cnt.count(2)])

students = sorted(students, key=lambda x: (x[2], -x[0], x[1]))

money = students[:n//4]
last = [student[1] for student in students if student[2] > 2]

print(money[-1][1], last[0])