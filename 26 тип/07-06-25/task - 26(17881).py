with open ('26_17881.txt') as file:
    n = int(file.readline())
    students = []
    for i in file:
        id0, ex1, ex2, ex3, ex4 = map(int, i.split())
        students.append([])