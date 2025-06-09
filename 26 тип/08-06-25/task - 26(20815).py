with open ('26_20815.txt') as file:
    n, k = map(int, file.readline().split())
    students = []
    for i in file:
        ID, ex1, ex2, ex3, ball = map(int, i.split())
        students.append([ex1 + ex2 + ex3 + ball, ball, ID])

students = sorted(students, key=lambda x: (-x[0], -x[1], x[2]))

if students[k-1][0] == students[k][0]:
    last = [student[2] for student in students if student[0] > students[k-1][0]][-1]
    cnt = len([1 for student in students if student[0] == students[k][0]])
else:
    last = students[k-1][0]
    cnt = 0


print(last, cnt)