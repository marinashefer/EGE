with open ('26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    students = []
    for i in file:
        ID, ex1, ex2, ex3, ball = map(int, i.split())
        students.append([ex1+ex2+ex3, ball, ID])

students = sorted(students, key=lambda x: (-x[0], -x[1], x[2]))

if students[s-1][0] == students[s][0]:
    last_id = [student[2] for student in students if student[0] > students[s-1][0]][-1]
    cnt = len([1 for student in students if student[0] == students[s][0]])
else:
    last_id = students[s-1][2]
    cnt = 0

print(last_id, cnt)