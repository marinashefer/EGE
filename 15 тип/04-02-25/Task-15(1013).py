from itertools import combinations

def f(x):
    P = 23 <= x < 45
    Q = 34 <= x <= 56
    A = A1 <= x <= A2
    return (not A) or (not P) and Q

ans = []

line = [x/10 for x in range(20*10, 60*10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(max(ans))