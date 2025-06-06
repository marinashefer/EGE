from itertools import combinations


def f(x):
    P = 15 <= x <= 33
    Q = 35 <= x <= 48
    A = A1 <= x <= A2
    return (A and (not Q)) <= (P or Q)

ans = []
line = [x/10 for x in range(10*10, 50*10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2-A1)

print(max(ans))