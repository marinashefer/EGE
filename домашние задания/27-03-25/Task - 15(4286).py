from itertools import combinations

def f(x):
    p = 1 <= x <= 98
    q = 25 <= x <= 42
    a = a1 <= x <= a2
    return q <= (not(p and q <= a))

ans = []
line = [x/5 for x in range(1*5, 98*5)]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(min(ans))
