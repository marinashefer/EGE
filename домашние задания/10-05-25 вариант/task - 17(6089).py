with open('17_6089.txt') as file:
    data = [int(i) for i in file]

maxx = max([i for i in data if str(i)[-1] == '2'])

def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    return res

ans = []
for i in range(len(data)):
    if abs(data[i]) % 3 == 0:
        if abs(data[i]) % 7 != 0:
            if abs(data[i])  % 17 != 0:
                if abs(data[i]) in f(maxx):
                    ans.append(data[i])

print(len(ans), max(ans))