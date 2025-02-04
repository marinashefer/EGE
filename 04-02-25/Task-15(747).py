from itertools import combinations

def f(x):
    P = 43 <= x <= 49
    Q = 44 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

ans = []
line = [x/10 for x in range(40*10, 60*10)] # [30, 43, 44, 49, 53, 60]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line): # all(f(x / 10) for x in range(A1 * 10 -1, A2 * 10 + 1)):
        ans.append(A2 - A1)

print(max(ans))