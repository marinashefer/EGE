with open ('17.txt') as file:
    num = [int(i) for i in file]

num_minimum = [x for x in num if x % 1 == 0]
minimum = min(num_minimum)

ans = []
for i in range(len(num) - 1):
    first = num[i]
    second = num[i] + 1
    if (first**2 < minimum**2) + (second**2 < minimum**2) == 1:
        summa = first + second
        if summa >= 0:
            ans.append(summa)

print(len(ans), min(ans))
